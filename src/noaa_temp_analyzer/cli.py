"""Command-line interface for noaa-temp-analyzer."""

import logging

import click


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
    click.echo("Data loading and analysis will be connected later.")
