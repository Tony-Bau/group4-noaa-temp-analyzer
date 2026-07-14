"""Tests for analyzing cleaned NOAA temperature data."""

import pandas as pd
import pytest

from noaa_temp_analyzer.analysis import (
    calculate_temperature_statistics,
    format_statistics,
)


def test_calculate_temperature_statistics_returns_expected_values() -> None:
    """Test that temperature statistics are calculated correctly."""
    data = pd.DataFrame({"temperature_celsius": [10.0, 20.0, 30.0]})

    statistics = calculate_temperature_statistics(data)

    assert statistics["count"] == 3
    assert statistics["mean"] == 20.0
    assert statistics["minimum"] == 10.0
    assert statistics["maximum"] == 30.0
    assert statistics["median"] == 20.0


def test_calculate_temperature_statistics_raises_on_missing_column() -> None:
    """Test that an error is raised if the required column is missing."""
    data = pd.DataFrame({"daytime": ["2023-01-01"]})

    with pytest.raises(ValueError, match="temperature_celsius"):
        calculate_temperature_statistics(data)


def test_calculate_temperature_statistics_raises_on_empty_data() -> None:
    """Test that an error is raised if the data is empty."""
    data = pd.DataFrame({"temperature_celsius": []})

    with pytest.raises(ValueError, match="No valid temperature values"):
        calculate_temperature_statistics(data)


def test_format_statistics_contains_all_expacted_lines() -> None:
    """Test that the formatted statistics contain all expected lables and values."""
    statistics = {
        "count": 3,
        "mean": 20.0,
        "minimum": 10.0,
        "maximum": 30.0,
        "median": 20.0,
        "standard_deviation": 10.0,
    }

    formatted = format_statistics(statistics)

    assert "Valid measurements: 3" in formatted
    assert "Mean temperature: 20.0 °C" in formatted
    assert "Minimum temperature: 10.0 °C" in formatted
    assert "Maximum temperature: 30.0 °C" in formatted
    assert "Median temperature: 20.0 °C" in formatted
    assert "Standard deviation: 10.0 °C" in formatted
