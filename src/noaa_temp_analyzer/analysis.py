"""Analyze cleaned temperature data."""

import logging
from typing import Any

import pandas as pd


LOGGER = logging.getLogger(__name__)


def calculate_temperature_statistics(data: pd.DataFrame) -> dict[str, Any]:
    """Calculate basic statistics for temperature data."""
    if "temperature_celsius" not in data.columns:
        raise ValueError("Data must contain 'temperature_celsius' column.")

    temperatures = data["temperature_celsius"]

    if temperatures.empty:
        raise ValueError("No valid temperature values available.")

    LOGGER.info("Calculating temperature statistics.")

    return {
        "count": int(temperatures.count()),
        "mean": round(float(temperatures.mean()), 2),
        "minimum": round(float(temperatures.min()), 2),
        "maximum": round(float(temperatures.max()), 2),
        "median": round(float(temperatures.median()), 2),
        "standard_deviation": round(float(temperatures.std()), 2),
    }


def format_statistics(statistics: dict[str, Any]) -> str:
    """Format temperature statistics as readable text."""
    return (
        "Temperature statistics\n"
        "----------------------\n"
        f"Valid measurements: {statistics['count']}\n"
        f"Mean temperature: {statistics['mean']} °C\n"
        f"Minimum temperature: {statistics['minimum']} °C\n"
        f"Maximum temperature: {statistics['maximum']} °C\n"
        f"Median temperature: {statistics['median']} °C\n"
        f"Standard deviation: {statistics['standard_deviation']} °C"
    )
