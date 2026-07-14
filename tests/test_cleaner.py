"""Tests for cleaning NOAA temperature data."""

import pandas as pd
import pytest
from noaa_temp_analyzer.cleaner import clean_temperature_data

def test_clean_temperature_data_converts_to_celsius() -> None:
    """Test that temperatures are converted from tenths of a degree to Celsius."""
    data = pd.DataFrame(
        {
            "datetime": ["2023-01-01", "2023-01-02"],
            "temperature": [100, 200],
        }
    )

    cleaned = clean_temperature_data(data)
    assert list(cleaned["temperature_celsius"]) == [10.0, 20.0]

def test_clean_temperature_data_removes_missing_values() -> None:
    """Test that rows with the missing value marker are removed."""
    data = pd.DataFrame(
        {
            "datetime": ["2023-01-01", "2023-01-02", "2023-01-03"],
            "temperature": [100, -9999, 200],
        }
    )

    cleaned = clean_temperature_data(data)
    assert len(cleaned) == 2
    assert -9999 not in cleaned["temperature_celsius"].values

def test_clean_temperatures_data_drops_missing_rows() -> None:
    """Test that rows with NaN are dropped."""
    data = pd.DataFrame(
        {
            "datetime": ["2023-01-01", None],
            "temperature": [100, 200],
        }
    )

    cleaned = clean_temperature_data(data)
    assert len(cleaned) == 1

def test_clean_temperature_data_sorts_by_datetime() -> None:
    """Test that the data is sorted by datetime."""
    data = pd.DataFrame(
        {
            "datetime": ["2023-01-02", "2023-01-01"],
            "temperature": [200, 100],
        }
    )

    cleaned = clean_temperature_data(data)
    assert list(cleaned["datetime"]) == ["2023-01-01", "2023-01-02"]

def test_clean_temperatures_data_raises_on_missing_columns() -> None:
    """Test that a ValueError is raised if required columns are missing."""
    data = pd.DataFrame({"datetime": ["2023-01-01"]})

    with pytest.raises(ValueError, match="datetime.*temperature"):
        clean_temperature_data(data)