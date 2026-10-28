from pathlib import Path

from dj_library_manager.config import INBOX_DIR, SUPPORTED_EXTENSIONS


def scan_inbox(inbox_dir: Path = INBOX_DIR) -> list[Path]:
    """Return all supported audio files found in the inbox."""

    if not inbox_dir.exists():
        raise FileNotFoundError(f"Inbox does not exist: {inbox_dir}")

    if not inbox_dir.is_dir():
        raise NotADirectoryError(f"Inbox path is not a folder: {inbox_dir}")

    audio_files = [
        file_path
        for file_path in inbox_dir.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    return sorted(audio_files)
