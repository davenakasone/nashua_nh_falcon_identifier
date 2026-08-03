"""photo_intake -- ingest falcon photos into a stable, de-duplicated catalog.

Standalone: ``python -m photo_intake ingest ~/Downloads/falcons --site nashua-downtown``.
Library: ``from photo_intake import ingest, load_catalog``.

The tool is deliberately dumb about falcons. It reads pixels and EXIF, assigns
each photo a stable id, and writes two records: a **public** catalog row (safe
to commit) and a **private** row holding GPS + the original absolute path
(gitignored). Deciding *which bird* is in a photo is the analysis layer's job,
not this tool's -- see ``docs/id_method.md``.
"""
from . import core
from .core import (
    PhotoIntakeError,
    PhotoRecord,
    dhash,
    ingest,
    load_catalog,
    read_metadata,
    sha256_file,
)

__all__ = [
    "ingest",
    "load_catalog",
    "read_metadata",
    "dhash",
    "sha256_file",
    "PhotoRecord",
    "PhotoIntakeError",
    "core",
]
