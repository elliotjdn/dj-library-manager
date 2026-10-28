from dataclasses import dataclass
from pathlib import Path


@dataclass
class Track:
    file_path: Path
    filename: str
    extension: str

    artist: str | None = None
    title: str | None = None
    album: str | None = None
    genre: str | None = None
