"""Clean NOAA temperature data."""

import logging

import pandas as pd


LOGGER = logging.getLogger(__name__)

MISSING_VALUE = -9999
TEMPERATURE_SCALE = 10


def clean_temperature_data(data: pd.DataFrame) -> pd.DataFrame:
    """Remove invalid temperatures and convert values to degrees Celsius."""
    required_columns = {"datetime", "temperature"}

    if not required_columns.issubset(data.columns):
        raise ValueError("Data must contain 'datetime' and 'temperature' columns.")

    cleaned = data.copy()
    original_count = len(cleaned)

    cleaned = cleaned.dropna(subset=["datetime", "temperature"])
    cleaned = cleaned[cleaned["temperature"] != MISSING_VALUE]

    cleaned["temperature_celsius"] = cleaned["temperature"] / TEMPERATURE_SCALE

    cleaned = cleaned[["datetime", "temperature_celsius"]]
    cleaned = cleaned.sort_values("datetime").reset_index(drop=True)

    removed_count = original_count - len(cleaned)
    LOGGER.info("Removed %s invalid temperature values.", removed_count)

    return cleaned
