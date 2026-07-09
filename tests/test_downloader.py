"""Tests for downloading NOAA ISD-Lite data files."""

from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from noaa_temp_analyzer.downloader import download_isd_lite_file


def test_download_isd_lite_file_returns_existing_file(tmp_path: Path) -> None:
    """Test that an existing file is reused instead of downloaded again."""
    existing_file = tmp_path / "10468099999-2023.gz"
    existing_file.write_bytes(b"cached content")

    with patch("noaa_temp_analyzer.downloader.requests.get") as mock_get:
        result = download_isd_lite_file("10468099999", 2023, output_dir=tmp_path)

    mock_get.assert_not_called()
    assert result == existing_file
    assert result.read_bytes() == b"cached content"


def test_download_isd_lite_file_downloads_and_saves(tmp_path: Path) -> None:
    """Test that a new file is downloaded and written to disk."""
    mock_response = Mock(status_code=200, content=b"new content")
    mock_response.raise_for_status = Mock()

    with patch(
        "noaa_temp_analyzer.downloader.requests.get", return_value=mock_response
    ) as mock_get:
        result = download_isd_lite_file("10468099999", 2023, output_dir=tmp_path)

    mock_get.assert_called_once()
    assert result.exists()
    assert result.read_bytes() == b"new content"


def test_download_isd_lite_file_raises_on_404(tmp_path: Path) -> None:
    """Test that a FileNotFoundError is raised when the server returns 404."""
    mock_response = Mock(status_code=404)

    with patch(
        "noaa_temp_analyzer.downloader.requests.get", return_value=mock_response
    ):
        with pytest.raises(FileNotFoundError, match="No data found"):
            download_isd_lite_file("10468099999", 2023, output_dir=tmp_path)


def test_download_isd_lite_file_creates_output_dir(tmp_path: Path) -> None:
    """Test that the output directory is created if it does not exist."""
    new_dir = tmp_path / "nested" / "data"
    mock_response = Mock(status_code=200, content=b"content")
    mock_response.raise_for_status = Mock()

    with patch(
        "noaa_temp_analyzer.downloader.requests.get", return_value=mock_response
    ):
        download_isd_lite_file("10468099999", 2023, output_dir=new_dir)

    assert new_dir.exists()
