from pathlib import Path

import pytest

from dj_library_manager.file_management.scanner import scan_inbox


def test_finds_supported_audio_files(tmp_path: Path):
    mp3_file = tmp_path / "track.mp3"
    wav_file = tmp_path / "mix.wav"

    mp3_file.touch()
    wav_file.touch()

    result = scan_inbox(tmp_path)

    assert result == sorted([mp3_file, wav_file])


def test_ignores_unsupported_files(tmp_path: Path):
    audio_file = tmp_path / "track.mp3"
    text_file = tmp_path / "notes.txt"

    audio_file.touch()
    text_file.touch()

    result = scan_inbox(tmp_path)

    assert result == [audio_file]
    assert text_file not in result


def test_ignores_folders(tmp_path: Path):
    audio_file = tmp_path / "track.mp3"
    folder_with_audio_extension = tmp_path / "folder.mp3"

    audio_file.touch()
    folder_with_audio_extension.mkdir()

    result = scan_inbox(tmp_path)

    assert result == [audio_file]


def test_empty_inbox_returns_empty_list(tmp_path: Path):
    result = scan_inbox(tmp_path)

    assert result == []


def test_missing_inbox_raises_error(tmp_path: Path):
    missing_inbox = tmp_path / "missing"

    with pytest.raises(FileNotFoundError):
        scan_inbox(missing_inbox)


def test_file_path_raises_error(tmp_path: Path):
    file_path = tmp_path / "not_a_folder"
    file_path.touch()

    with pytest.raises(NotADirectoryError):
        scan_inbox(file_path)
