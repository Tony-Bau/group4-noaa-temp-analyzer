"""Tests for the command-line interface."""

from click.testing import CliRunner
from unittest.mock import Mock, patch

from noaa_temp_analyzer.cli import main


def test_cli_runs_with_required_arguments() -> None:
    """Test that the CLI runs with the required arguments."""
    runner = CliRunner()

    with patch("noaa_temp_analyzer.cli.download_isd_lite_file", return_value="data/test.gz"), \
         patch("noaa_temp_analyzer.cli.load_isd_lite_data", return_value="raw_data"), \
         patch("noaa_temp_analyzer.cli.clean_temperature_data", return_value="cleaned_data"), \
         patch(
             "noaa_temp_analyzer.cli.calculate_temperature_statistics",
             return_value={
                 "count": 2,
                 "mean": 15.0,
                 "minimum": 10.0,
                 "maximum": 20.0,
                 "median": 15.0,
                 "standard_deviation": 7.07,
             },
         ), \
         patch(
             "noaa_temp_analyzer.cli.format_statistics",
             return_value="Temperature statistics\nValid measurements: 2",
         ):
        result = runner.invoke(
            main,
            ["--station", "10468099999", "--year", "2023", "--text-only"],
        )

    assert result.exit_code == 0
    assert "NOAA Temperature Analyzer" in result.output
    assert "Station: 10468099999" in result.output
    assert "Year: 2023" in result.output
    assert "Text-only mode: enabled" in result.output
    assert "Temperature statistics" in result.output
    assert "Valid measurements: 2" in result.output


def test_cli_saves_plot_when_not_text_only() -> None:
    """Test that the CLI creates and saves a plot when graphics are enabled."""
    runner = CliRunner()
    fake_figure = Mock()

    with patch("noaa_temp_analyzer.cli.download_isd_lite_file", return_value="data/test.gz"), \
         patch("noaa_temp_analyzer.cli.load_isd_lite_data", return_value="raw_data"), \
         patch("noaa_temp_analyzer.cli.clean_temperature_data", return_value="cleaned_data"), \
         patch(
             "noaa_temp_analyzer.cli.calculate_temperature_statistics",
             return_value={
                 "count": 2,
                 "mean": 15.0,
                 "minimum": 10.0,
                 "maximum": 20.0,
                 "median": 15.0,
                 "standard_deviation": 7.07,
             },
         ), \
         patch(
             "noaa_temp_analyzer.cli.format_statistics",
             return_value="Temperature statistics\nValid measurements: 2",
         ), \
         patch(
             "noaa_temp_analyzer.cli.plot_temperature_over_time",
             return_value=fake_figure,
         ) as mock_plot, \
         patch("noaa_temp_analyzer.cli.save_plot") as mock_save:
        result = runner.invoke(
            main,
            ["--station", "10468099999", "--year", "2023"],
        )

    assert result.exit_code == 0
    mock_plot.assert_called_once()
    mock_save.assert_called_once()
    assert "Plot saved to:" in result.output


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
