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


def read_photo_gps() -> list[dict]:
    """Photo GPS from the gitignored intake sidecar, joined to the catalog.

    **A photo's GPS locates the photographer, not the bird** -- which is more
    useful here than it sounds. Combined with the compass heading some phones
    write (``GPSImgDirection``), each geotagged frame is a ray pointing at the
    perch, and rays from two standing positions triangulate it.

    It is also the only reliable way to separate Nashua frames from photos taken
    on trips elsewhere: habitat and tower shots look alike, coordinates do not.
    """
    priv = ROOT / "private" / "locations.csv"
    if not priv.exists():
        return []
    with open(priv, newline="", encoding="utf-8-sig") as fh:
        rows = [r for r in csv.DictReader(fh)]
    cat = {}
    if (ROOT / "data" / "photos.csv").exists():
        with open(ROOT / "data" / "photos.csv", newline="", encoding="utf-8-sig") as fh:
            cat = {r["photo_id"]: r for r in csv.DictReader(fh)}
    out = []
    for r in rows:
        try:
            float(r.get("lat") or ""), float(r.get("lon") or "")
        except ValueError:
            continue  # blank or malformed coordinate: skip, do not crash the map
        meta = cat.get(r["photo_id"], {})
        out.append({**r, "captured_at": meta.get("captured_at", ""),
                    "site": meta.get("site", ""), "observer": meta.get("observer", ""),
                    "individual": meta.get("individual", "")})
    return out


def read_coords() -> list[dict]:
    if not COORDS.exists():
        sys.exit(f"missing {COORDS.relative_to(ROOT)} — see the module docstring")
    with open(COORDS, newline="", encoding="utf-8-sig") as fh:
        return [r for r in csv.DictReader(fh)]


def read_sightings() -> list[dict]:
    if not SIGHTINGS.exists():
        return []
    with open(SIGHTINGS, newline="", encoding="utf-8-sig") as fh:
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

    downtown = [c for c in coords if c["cluster"] == "nashua-downtown"]
    if not downtown:
        sys.exit("no downtown Nashua records — nothing to map")

    def _f(rows, key):
        out = []
        for r in rows:
            try:
                out.append(float(r[key]))
            except (KeyError, ValueError):
                pass
        return out

    lats, lons = _f(downtown, "lat"), _f(downtown, "lon")
    if not lats or not lons:
        sys.exit("downtown records carry no usable coordinates")
    centre = (sum(lats) / len(lats), sum(lons) / len(lons))

    m = folium.Map(location=centre, zoom_start=16, tiles=None)
    folium.TileLayer(ESRI, attr="Esri World Imagery", name="Aerial (Esri)",
                     max_zoom=19).add_to(m)
    folium.TileLayer("OpenStreetMap", name="Street").add_to(m)

    # --- sightings -------------------------------------------------------
    obs = folium.FeatureGroup(name="Peregrine sightings (eBird, 30d)").add_to(m)
    for c in coords:
        try:
            lat, lon = float(c["lat"]), float(c["lon"])
        except ValueError:
            continue
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

    # --- where the photos were taken -------------------------------------
    photos = read_photo_gps()
    if photos:
        fg = folium.FeatureGroup(name=f"Photo positions ({len(photos)})").add_to(m)
        far = 0
        for p in photos:
            lat, lon = float(p["lat"]), float(p["lon"])
            away = _haversine(centre[0], centre[1], lat, lon)
            if away > 50:
                far += 1
            folium.Marker(
                (lat, lon), icon=folium.Icon(
                    color="red" if away > 50 else "green", icon="camera", prefix="fa"),
                popup=folium.Popup(
                    f"<b>{p['photo_id']}</b><br>{p.get('captured_at','?')}"
                    f"<br>site: {p.get('site') or '-'}"
                    f"<br>observer: {p.get('observer') or '-'}"
                    f"<br>{away:.1f} km from the downtown centroid"
                    + ("<br><b style='color:#c00'>NOT A NASHUA PHOTO</b>" if away > 50 else ""),
                    max_width=300),
                tooltip=f"{p['photo_id']} ({away:.1f} km)",
            ).add_to(fg)
        print(f"  {len(photos)} geotagged photo(s)"
              + (f", {far} more than 50 km away — NOT Nashua" if far else ""))
    else:
        print("  no geotagged photos yet — see read_photo_gps() docstring")

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
    print(f"  activity envelope ~{max(span_km, 0.4)*1000:.0f} m radius (as drawn)")
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


# --------------------------------------------------------------------------
# bearing triangulation
# --------------------------------------------------------------------------
#: Magnetic declination for Nashua NH, 2026 (west is negative).
#: **Phones write MAGNETIC bearings** (`GPSImgDirectionRef: M`), so every ray
#: must be rotated by this before use. Skipping it silently smears the solution.
DECLINATION_DEG = -14.3


def triangulate(rays, min_angle=20, max_range_m=1500, cell_m=20):
    """Where do the camera bearings converge?

    ``rays`` is ``[(lat, lon, true_bearing_deg), ...]`` — a photographer's
    position and where the camera was pointed. Each pair of rays that meet at a
    usable angle gives a candidate subject position; dense clusters of those
    are structures the group photographs repeatedly.

    **This is a lead, not a location.** Three things bound it: phone compasses
    are good to maybe ±10–20° and worse beside steel (a millyard and a lattice
    tower are the worst case), the declination above is a model value not a
    measurement, and near-parallel pairs are numerically unstable — which is
    why ``min_angle`` rejects them. At 100 m a 15° error is ±26 m, so cluster
    centres are about as precise as the cells they fall in.

    Returns ``[((lat, lon), hits), ...]`` densest first.
    """
    import itertools
    if len(rays) < 2:
        return []
    lat0 = sum(r[0] for r in rays) / len(rays)
    lon0 = sum(r[1] for r in rays) / len(rays)
    mlat, mlon = 111320.0, 111320.0 * math.cos(math.radians(lat0))
    local = [(((lo - lon0) * mlon), ((la - lat0) * mlat), b) for la, lo, b in rays]

    hits = []
    for (x1, y1, b1), (x2, y2, b2) in itertools.combinations(local, 2):
        sep = abs(((b1 - b2 + 180) % 360) - 180)
        if sep < min_angle or sep > 180 - min_angle:
            continue
        d1 = (math.sin(math.radians(b1)), math.cos(math.radians(b1)))
        d2 = (math.sin(math.radians(b2)), math.cos(math.radians(b2)))
        den = d1[0] * -d2[1] - d1[1] * -d2[0]
        if abs(den) < 1e-6:
            continue
        t = ((x2 - x1) * -d2[1] - (y2 - y1) * -d2[0]) / den
        u = (d1[0] * (y2 - y1) - d1[1] * (x2 - x1)) / den
        if not (5 < t < max_range_m and 5 < u < max_range_m):
            continue          # forward along both rays only
        hits.append((x1 + t * d1[0], y1 + t * d1[1]))

    from collections import Counter
    grid = Counter((round(x / cell_m), round(y / cell_m)) for x, y in hits)
    return [((lat0 + gy * cell_m / mlat, lon0 + gx * cell_m / mlon), n)
            for (gx, gy), n in grid.most_common()]
