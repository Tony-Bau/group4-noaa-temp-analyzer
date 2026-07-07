"""Tests for the command-line interface."""

from click.testing import CliRunner

from noaa_temp_analyzer.cli import main


def test_cli_runs_with_required_arguments() -> None:
    """Test that the CLI runs with the required arguments."""
    runner = CliRunner()

    result = runner.invoke(
        main,
        ["--station", "10468099999", "--year", "2023", "--text-only"],
    )

    assert result.exit_code == 0
    assert "NOAA Temperature Analyzer" in result.output
    assert "Station: 10468099999" in result.output
    assert "Year: 2023" in result.output
    assert "Text-only mode: enabled" in result.output


def test_cli_requires_station() -> None:
    """Test that the CLI fails if the station option is missing."""
    runner = CliRunner()

    result = runner.invoke(main, ["--year", "2023", "--text-only"])

    assert result.exit_code != 0
    assert "Missing option '--station'" in result.output


def test_cli_requires_year() -> None:
    """Test that the CLI fails if the year option is missing."""
    runner = CliRunner()

    result = runner.invoke(main, ["--station", "10468099999", "--text-only"])

    assert result.exit_code != 0
    assert "Missing option '--year'" in result.output
