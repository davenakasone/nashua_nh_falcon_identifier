#!/usr/bin/env python3
"""Map the Nashua peregrine search area — sightings, perches, nest candidates.

    ~/dkn314/bin/python nest_map.py

Purpose: give the nest hunt a target list instead of a vibe. The group's plan is
to shortlist rooftops from aerial imagery and then send a City-cleared drone
pilot to the shortlist; this map is the shortlist, with every confirmed sighting
plotted so the candidates can be judged against where the birds actually are.

**Offline and keyless.** It reads coordinates from ``private/locations_named.csv``
(gitignored, produced from an eBird pull) and the observation record from
``data/sightings.csv``. It does not talk to eBird itself — per ../RULES.md a tool
owns its own networking or does none, and this one does none.

**Output is gitignored on purpose.** ``out/nest_map.html`` carries coordinates,
so it stays out of the public repo. Share the file directly with the group; do
not commit it. See ``data/README.md``.

Basemaps: OpenStreetMap plus Esri World Imagery — the aerial layer is the one
that matters here, since the question is what the roofs look like.
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import folium

ROOT = Path(__file__).resolve().parent
COORDS = ROOT / "private" / "locations_named.csv"
SIGHTINGS = ROOT / "data" / "sightings.csv"
OUT = ROOT / "out" / "nest_map.html"

ESRI = ("https://server.arcgisonline.com/ArcGIS/rest/services/"
        "World_Imagery/MapServer/tile/{z}/{y}/{x}")

#: Structures the group has named, with the state of the search on each.
#: Coordinates deliberately absent — they should come from the Nashua City GIS
#: 2024 aerial survey, not from a guess. Placed on the map only once known.
CANDIDATES = [
    ("Clock Tower", "candidate",
     "Strongest ground-level guess. Central to every confirmed sighting; birds "
     "use the weathervane and rails. Possible entry to the clock mechanism "
     "space, which humans visit only for repairs. Pigeons are everywhere on "
     "surrounding buildings but NEVER on this tower — real negative evidence."),
    ("Millyard smokestack", "candidate",
     "NH Audubon: if the chimney is inactive and capped, dust and vegetation "
     "accumulate on top and a scrape could sit there. Cannot be confirmed from "
     "the ground. Confirmed perch for the male."),
    ("Circular chimney across the river", "candidate",
     "Near the apartments. In regular use as a perch at dusk."),
    ("Mill Building No 1 / Clocktower Apartments, north alley side", "candidate",
     "Little human traffic, many ledges. North aspect is a mark against it."),
    ("Clock Tower — ingress inspection", "checked-negative",
     "2026-07-24: looked for a missing brick or a roof gap, none found. Not "
     "ruled out — long building, multiple turrets."),
    ("99 Factory Street (abandoned)", "ruled-out",
     "Too many pigeons roosting inside; falcons would not tolerate that at a "
     "nest site."),
]

#: David: a falcon is always visible at the radio tower or a chimney, and at
#: sunset they move north-east. Drawn as a search vector, not a fact.
DUSK_BEARING_DEG = 45
DUSK_RAY_KM = 2.0


def read_coords() -> list[dict]:
    if not COORDS.exists():
        sys.exit(f"missing {COORDS.relative_to(ROOT)} — see the module docstring")
    with open(COORDS, newline="") as fh:
        return [r for r in csv.DictReader(fh)]


def read_sightings() -> list[dict]:
    if not SIGHTINGS.exists():
        return []
    with open(SIGHTINGS, newline="") as fh:
        return [r for r in csv.DictReader(fh)]


def destination(lat: float, lon: float, bearing_deg: float, km: float):
    """Point `km` away along `bearing_deg` — great-circle, good enough at 2 km."""
    r = 6371.0
    b, p1, l1 = map(math.radians, (bearing_deg, lat, lon))
    d = km / r
    p2 = math.asin(math.sin(p1) * math.cos(d) + math.cos(p1) * math.sin(d) * math.cos(b))
    l2 = l1 + math.atan2(math.sin(b) * math.sin(d) * math.cos(p1),
                         math.cos(d) - math.sin(p1) * math.sin(p2))
    return math.degrees(p2), math.degrees(l2)


def main() -> int:
    coords = read_coords()
    sightings = {(s["date"][:10], s["site"]): s for s in read_sightings()}

    downtown = [c for c in coords if c["cluster"] == "nashua-downtown"]
    if not downtown:
        sys.exit("no downtown Nashua records — nothing to map")

    lats = [float(c["lat"]) for c in downtown]
    lons = [float(c["lon"]) for c in downtown]
    centre = (sum(lats) / len(lats), sum(lons) / len(lons))

    m = folium.Map(location=centre, zoom_start=16, tiles=None)
    folium.TileLayer(ESRI, attr="Esri World Imagery", name="Aerial (Esri)",
                     max_zoom=19).add_to(m)
    folium.TileLayer("OpenStreetMap", name="Street").add_to(m)

    # --- sightings -------------------------------------------------------
    obs = folium.FeatureGroup(name="Peregrine sightings (eBird, 30d)").add_to(m)
    for c in coords:
        lat, lon = float(c["lat"]), float(c["lon"])
        n = c["count"] or "?"
        near = c["cluster"] == "nashua-downtown"
        folium.CircleMarker(
            (lat, lon), radius=8 if near else 5,
            color="#d94801" if near else "#6a6a6a",
            fill=True, fill_opacity=0.85 if near else 0.5,
            popup=folium.Popup(
                f"<b>{c['loc']}</b><br>{c['date']}<br>count: {n}"
                f"<br><i>{c['cluster']}</i>", max_width=320),
            tooltip=f"{c['date'][:10]} · {n} bird(s)",
        ).add_to(obs)

    # --- the search area -------------------------------------------------
    span_km = max(
        _haversine(centre[0], centre[1], la, lo) for la, lo in zip(lats, lons)
    )
    folium.Circle(
        centre, radius=max(span_km, 0.4) * 1000, color="#2b8cbe", weight=2,
        fill=True, fill_opacity=0.06,
        popup="Downtown Nashua activity envelope — all confirmed sightings fall inside",
    ).add_to(folium.FeatureGroup(name="Search area").add_to(m))

    # --- the dusk vector -------------------------------------------------
    dusk = folium.FeatureGroup(name="Dusk departure bearing (approximate)").add_to(m)
    end = destination(centre[0], centre[1], DUSK_BEARING_DEG, DUSK_RAY_KM)
    folium.PolyLine(
        [centre, end], color="#762a83", weight=3, dash_array="8,6",
        popup=("Observer report: at sunset the birds move NORTH-EAST, distance "
               "unknown. Drawn from the sighting centroid, not from a surveyed "
               "standing position — treat as a search vector, not a measurement. "
               "Peregrines usually roost at or near the nest, so where they go "
               "after dark is a lead on the scrape."),
    ).add_to(dusk)

    # --- candidate structures -------------------------------------------
    colour = {"candidate": "#1a9850", "checked-negative": "#f0a30a",
              "ruled-out": "#999999"}
    rows = "".join(
        f'<tr><td style="color:{colour[s]};font-weight:bold">&#9632;</td>'
        f'<td><b>{n}</b><br><span style="font-size:11px">{d}</span></td></tr>'
        for n, s, d in CANDIDATES)
    legend = f"""
    <div style="position:fixed;bottom:18px;left:18px;z-index:9999;background:#fff;
                padding:10px 12px;border:1px solid #888;border-radius:6px;
                max-width:380px;max-height:46vh;overflow:auto;
                font:12px/1.35 -apple-system,sans-serif">
      <div style="font-weight:bold;margin-bottom:6px">Nest candidates</div>
      <table style="border-spacing:4px 3px">{rows}</table>
      <div style="margin-top:8px;font-size:11px;color:#555">
        Structures are <b>not plotted</b> — their coordinates should come from the
        Nashua City GIS 2024 aerial survey, not from a guess. Switch to the aerial
        layer to scout roofs.
      </div>
    </div>"""
    m.get_root().html.add_child(folium.Element(legend))

    folium.LayerControl(collapsed=False).add_to(m)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    m.save(str(OUT))
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(downtown)} downtown record(s), "
          f"{len(coords) - len(downtown)} Bedford/Manchester")
    print(f"  activity envelope ~{span_km*1000:.0f} m radius")
    print("  NOT committed — this file carries coordinates (see .gitignore)")
    return 0


def _haversine(lat1, lon1, lat2, lon2) -> float:
    r = 6371.0
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = (math.sin(dp / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(dl / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(a))


if __name__ == "__main__":
    sys.exit(main())
