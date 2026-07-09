"""Load NOAA ISD-Lite data files."""

import logging
from pathlib import Path

import pandas as pd


LOGGER = logging.getLogger(__name__)

COLUMN_NAMES = [
    "year",
    "month",
    "day",
    "hour",
    "temperature",
    "dew_point",
    "sea_level_pressure",
    "wind_direction",
    "wind_speed",
    "sky_condition",
    "precipitation_1h",
    "precipitation_6h",
]


def load_isd_lite_data(file_path: str | Path) -> pd.DataFrame:
    """Load an ISD-Lite file into a pandas DataFrame."""
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist: {file_path}")

    LOGGER.info("Loading file: %s", file_path)

    data = pd.read_csv(
        file_path,
        sep=r"\s+",
        names=COLUMN_NAMES,
        compression="infer",
        engine="python",
    )

    data["datetime"] = pd.to_datetime(
        data[["year", "month", "day", "hour"]],
        errors="coerce",
    )

    return data[["datetime", "temperature"]]