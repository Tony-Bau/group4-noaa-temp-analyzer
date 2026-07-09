"""Command-line interface for noaa-temp-analyzer."""

import logging
from pathlib import Path

import click

from noaa_temp_analyzer.analysis import (
    calculate_temperature_statistics,
    format_statistics,
)
from noaa_temp_analyzer.cleaner import clean_temperature_data
from noaa_temp_analyzer.downloader import download_isd_lite_file
from noaa_temp_analyzer.loader import load_isd_lite_data
from noaa_temp_analyzer.plotting import plot_temperature_over_time, save_plot


LOGGER = logging.getLogger(__name__)


def configure_logging(verbosity: int) -> None:
    """Configure logging based on the selected verbosity level."""
    if verbosity <= 0:
        level = logging.ERROR
    elif verbosity == 1:
        level = logging.WARNING
    elif verbosity == 2:
        level = logging.INFO
    else:
        level = logging.DEBUG

    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


@click.command()
@click.option(
    "--station",
    "station_id",
    required=True,
    help="Weather station ID to analyze.",
)
@click.option(
    "--year",
    required=True,
    type=int,
    help="Year of the weather data to analyze.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase verbosity. Use -v, -vv or -vvv.",
)
@click.option(
    "--text-only",
    is_flag=True,
    help="Run without showing graphics.",
)
def main(station_id: str, year: int, verbose: int, text_only: bool) -> None:
    """Run the noaa-temp-analyzer command-line interface."""
    configure_logging(verbose)

    LOGGER.warning("Warning logging is enabled.")
    LOGGER.info("Info logging is enabled.")
    LOGGER.debug("Debug logging is enabled.")

    click.echo("NOAA Temperature Analyzer")
    click.echo(f"Station: {station_id}")
    click.echo(f"Year: {year}")
    click.echo(f"Text-only mode: {'enabled' if text_only else 'disabled'}")
    click.echo()

    file_path = download_isd_lite_file(station_id, year)
    raw_data = load_isd_lite_data(file_path)
    cleaned_data = clean_temperature_data(raw_data)

    statistics = calculate_temperature_statistics(cleaned_data)
    click.echo(format_statistics(statistics))

    if not text_only:
        figure = plot_temperature_over_time(
            cleaned_data,
            title=f"Temperature for station {station_id} in {year}",
        )
        output_path = Path("plots") / f"{station_id}-{year}.png"
        save_plot(figure, output_path)
        click.echo()
        click.echo(f"Plot saved to: {output_path}")
