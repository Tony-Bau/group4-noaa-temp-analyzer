"""Download NOAA ISD-Lite data files."""

import logging
from pathlib import Path

import requests


LOGGER = logging.getLogger(__name__)

BASE_URL = "https://www.ncei.noaa.gov/pub/data/noaa/isd-lite"


def _format_station_id(station_id: str) -> str:
    """Convert an 11-digit station ID to NOAA's USAF-WBAN format."""
    if len(station_id) != 11 or not station_id.isdigit():
        raise ValueError(
            f"Station ID must be an 11-digit string, got: {station_id}"
        )

    return f"{station_id[:6]}-{station_id[6:]}"


def download_isd_lite_file(
    station_id: str,
    year: int,
    output_dir: str | Path = "data",
) -> Path:
    """Download an ISD-Lite file for a station and year."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    formatted_station_id = _format_station_id(station_id)
    file_name = f"{formatted_station_id}-{year}.gz"
    file_url = f"{BASE_URL}/{year}/{file_name}"
    output_path = output_dir / file_name

    if output_path.exists():
        LOGGER.info("Using existing file: %s", output_path)
        return output_path

    LOGGER.info("Downloading data from: %s", file_url)

    response = requests.get(file_url, timeout=30)

    if response.status_code == 404:
        raise FileNotFoundError(
            f"No data found for station {station_id} and year {year}."
        )

    response.raise_for_status()
    output_path.write_bytes(response.content)

    LOGGER.info("Saved downloaded file to: %s", output_path)

    return output_path
