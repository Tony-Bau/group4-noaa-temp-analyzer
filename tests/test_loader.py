"""Tests for loading NOAA ISD-Lite data files."""

from pathlib import Path

import pandas as pd
import pytest

from noaa_temp_analyzer.loader import load_isd_lite_data


def test_load_isd_lite_data_returns_datetime_and_temperature(tmp_path: Path) -> None:
    """Test that loading a valid file returns datetime and temperature columns."""
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "2023 01 01 00  100   50 10132    9    31  4    -9999 -9999\n"
        "2023 01 01 01  120   55 10130    8    28  4    -9999 -9999\n"
    )

    data = load_isd_lite_data(file_path)

    assert list(data.columns) == ["datetime", "temperature"]
    assert len(data) == 2
    assert data["temperature"].tolist() == [100, 120]


def test_load_isd_lite_data_parses_datetime_correctly(tmp_path: Path) -> None:
    """Test that the datetime column is correctly parsed from date parts."""
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "2023 06 15 12  200   60 10100    5    20  1    -9999 -9999\n"
    )

    data = load_isd_lite_data(file_path)

    assert data["datetime"].iloc[0] == pd.Timestamp("2023-06-15 12:00:00")


def test_load_isd_lite_data_raises_on_missing_file(tmp_path: Path) -> None:
    """Test that a FileNotFoundError is raised for a non-existent file."""
    missing_file = tmp_path / "does-not-exist.gz"

    with pytest.raises(FileNotFoundError, match="does not exist"):
        load_isd_lite_data(missing_file)
