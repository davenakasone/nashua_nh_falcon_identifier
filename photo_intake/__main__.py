"""Standalone CLI for photo_intake -- ``python -m photo_intake <command>``.

    python -m photo_intake ingest ~/Downloads/drop --site nashua-downtown \
        --observer david --perch white-bracket --store drive
    python -m photo_intake ingest one.jpg --dry-run   # look, don't write
    python -m photo_intake list --site nashua-downtown
    python -m photo_intake show 20260803-a1b2c3d4
    python -m photo_intake stats

The catalog lives under ``--root`` (default: this repo) as ``data/photos.csv``.
Precise GPS is never printed unless you pass ``--reveal-gps``, and never written
to the public catalog at all.

Originals are **not** copied by default -- the CSV row is the durable record and
the photos are expected to live in cold storage elsewhere. Pass ``--copy`` when
this machine should keep the bytes too.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table

from . import core

console = Console()
REPO_ROOT = Path(__file__).resolve().parent.parent


def cmd_ingest(args) -> int:
    result = core.ingest(
        args.paths,
        root=args.root,
        site=args.site,
        observer=args.observer,
        perch=args.perch,
        store=args.store,
        copy=args.copy,
        dry_run=args.dry_run,
    )
    added, dupes, near = result["added"], result["duplicates"], result["near"]

    if added:
        table = Table(title=f"ingested {len(added)}"
                            + (" (DRY RUN -- nothing written)" if args.dry_run else ""))
        for col in ("photo_id", "captured", "camera", "size", "gps", "source"):
            table.add_column(col, overflow="fold")
        for r in added:
            table.add_row(
                r.photo_id,
                (r.captured_at or "?") + ("" if r.date_source == "exif" else " *"),
                r.camera or "-",
                f"{r.width}x{r.height}" if r.width else "unreadable",
                "yes" if r.has_gps else "-",
                r.source_name,
            )
        console.print(table)
        if any(r.date_source != "exif" for r in added):
            console.print("[dim]* timestamp came from file mtime, not EXIF -- "
                          "treat the date as approximate.[/dim]")
        if any(r.has_gps for r in added):
            console.print("[dim]GPS found: coordinates went to private/locations.csv "
                          "(gitignored), never to the public catalog.[/dim]")
    else:
        console.print("[yellow]nothing new ingested[/yellow]")

    if dupes:
        console.print(f"[dim]skipped {len(dupes)} exact duplicate(s) already "
                      f"in the catalog[/dim]")
    for pid, other, distance in near:
        console.print(f"[cyan]near-duplicate[/cyan] {pid} ~ {other} "
                      f"({distance} bits) -- same frame or same burst, kept both")
    return 0


def cmd_list(args) -> int:
    rows = core.load_catalog(args.root)
    if args.site:
        rows = [r for r in rows if r.get("site") == args.site]
    if args.individual:
        rows = [r for r in rows if r.get("individual") == args.individual]
    if args.unassigned:
        rows = [r for r in rows if not r.get("individual")]
    if args.band_untested:
        rows = [r for r in rows if r.get("band_visible") in ("", "not-tested", None)]
    if args.since:
        rows = [r for r in rows if (r.get("captured_at") or "") >= args.since]
    rows.sort(key=lambda r: (r.get("captured_at") or "", r["photo_id"]))

    if not rows:
        console.print("[yellow]no photos match[/yellow]")
        return 0

    table = Table(title=f"{len(rows)} photo(s)")
    for col in ("photo_id", "captured", "site", "perch", "observer",
                "individual", "band"):
        table.add_column(col, overflow="fold")
    for r in rows:
        table.add_row(r["photo_id"], (r.get("captured_at") or "?")[:16],
                      r.get("site") or "-", r.get("perch") or "-",
                      r.get("observer") or "-",
                      r.get("individual") or "[dim]unassigned[/dim]",
                      r.get("band_code") or r.get("band_visible")
                      or "[dim]unreviewed[/dim]")
    console.print(table)
    return 0


def cmd_show(args) -> int:
    catalog = core.load_catalog(args.root)
    rows = {r["photo_id"]: r for r in catalog}
    if len(rows) != len(catalog):
        console.print("[yellow]warning: duplicate photo_ids in the catalog — "
                      "some rows are unreachable by id[/yellow]")
    match = rows.get(args.id)
    if match is None:
        hits = [r for k, r in rows.items() if k.startswith(args.id)]
        if not hits:
            console.print(f"[red]no photo with id starting {args.id!r}[/red]")
            return 1
        if len(hits) > 1:
            console.print(f"[red]{args.id!r} is ambiguous — {len(hits)} matches:[/red] "
                          + ", ".join(h["photo_id"] for h in hits[:10]))
            return 1
        match = hits[0]

    table = Table(title=match["photo_id"], show_header=False)
    table.add_column("field", style="bold")
    table.add_column("value", overflow="fold")
    for key, value in match.items():
        if key == "photo_id":
            continue
        table.add_row(key, str(value) if value not in (None, "") else "-")

    if args.reveal_gps:
        row = core.load_private(args.root).get(match["photo_id"], {})
        table.add_row("[red]lat[/red]", str(row.get("lat") or "-"))
        table.add_row("[red]lon[/red]", str(row.get("lon") or "-"))
        table.add_row("[red]source_path[/red]", str(row.get("source_path") or "-"))
    console.print(table)
    if core._bool_in(match.get("has_gps", "")) and not args.reveal_gps:
        console.print("[dim]this photo has GPS; --reveal-gps to print it[/dim]")
    return 0


def cmd_stats(args) -> int:
    rows = core.load_catalog(args.root)
    sightings = core.load_sightings(args.root)
    if not rows and not sightings:
        console.print("[yellow]catalog is empty -- nothing ingested yet[/yellow]")
        return 0

    def tally(key):
        counts: dict = {}
        for r in rows:
            name = r.get(key) or "unassigned"
            counts[name] = counts.get(name, 0) + 1
        return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    dates = sorted(r["captured_at"][:10] for r in rows if r.get("captured_at"))
    console.print(f"[bold]{len(rows)}[/bold] photos"
                  + (f", {dates[0]} to {dates[-1]}" if dates else "")
                  + f" · [bold]{len(sightings)}[/bold] sightings")

    for key in ("individual", "site", "perch", "observer"):
        if not rows:
            break
        table = Table(title=f"by {key}")
        table.add_column(key)
        table.add_column("photos", justify="right")
        for name, count in tally(key):
            table.add_row(str(name), str(count))
        console.print(table)

    untested = [r for r in rows if r.get("band_visible") in ("", "not-tested", None)]
    if untested:
        console.print(f"[yellow]{len(untested)} photo(s) have not resolved the "
                      f"band question[/yellow] -- the band zone is the tarsus, "
                      f"not the toes; see docs/id_method.md")
    unreadable = [r["photo_id"] for r in rows
                  if not core._bool_in(r.get("readable", ""))]
    if unreadable:
        console.print(f"[yellow]{len(unreadable)} unreadable "
                      f"(HEIC/RAW without a converter): {', '.join(unreadable[:5])}"
                      f"{' ...' if len(unreadable) > 5 else ''}[/yellow]")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="photo_intake", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT,
                        help="catalog root (default: the repo this tool lives in)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("ingest", help="add photos to the catalog")
    p.add_argument("paths", nargs="+", help="image files or directories")
    p.add_argument("--site", help="coarse location label, e.g. nashua-downtown")
    p.add_argument("--observer", help="who took them, e.g. david/jarrod/mark")
    p.add_argument("--perch", help="perch label, e.g. white-bracket")
    p.add_argument("--store", help="where the originals live, e.g. drive")
    p.add_argument("--copy", action="store_true",
                   help="also copy originals into photos/ on this machine")
    p.add_argument("--dry-run", action="store_true", help="report, write nothing")
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("list", help="list catalogued photos")
    p.add_argument("--site")
    p.add_argument("--individual")
    p.add_argument("--unassigned", action="store_true",
                   help="only photos not yet tied to an individual bird")
    p.add_argument("--band-untested", action="store_true",
                   help="only photos whose band question is still open")
    p.add_argument("--since", help="ISO date lower bound, e.g. 2026-08-01")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="everything about one photo (id or prefix)")
    p.add_argument("id")
    p.add_argument("--reveal-gps", action="store_true",
                   help="also print the private coordinates and source path")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("stats", help="catalog summary")
    p.set_defaults(func=cmd_stats)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except core.PhotoIntakeError as exc:
        console.print(f"[red]error:[/red] {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
