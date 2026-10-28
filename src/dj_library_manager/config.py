from pathlib import Path


# The main project folder: dj-library-manager/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Folders used while processing music
DATA_DIR = PROJECT_ROOT / "data"
INBOX_DIR = DATA_DIR / "inbox"
PROCESSED_DIR = DATA_DIR / "processed"
BACKUP_DIR = DATA_DIR / "backups"

# Audio formats the application currently accepts
SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aiff",
    ".m4a",
}


if __name__ == "__main__":
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Inbox: {INBOX_DIR}")
    print(f"Processed: {PROCESSED_DIR}")
    print(f"Backups: {BACKUP_DIR}")
    print(f"Inbox exists: {INBOX_DIR.exists()}")
