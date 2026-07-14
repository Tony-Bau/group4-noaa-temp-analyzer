import pandas as pd
from matplotlib.figure import Figure

from noaa_temp_analyzer.plotting import (
    plot_temperature_over_time,
    save_plot,
)


def test_plot_temperature_over_time_returns_figure():
    """Test that plotting returns a matplotlib figure."""
    data = pd.DataFrame(
        {
            "datetime": pd.date_range("2023-01-01", periods=5, freq="D"),
            "temperature_celsius": [1.0, 2.0, 3.0, 4.0, 5.0],
        }
    )

    fig = plot_temperature_over_time(data)

    assert isinstance(fig, Figure)


def test_save_plot_writes_file(tmp_path):
    """Test that save_plot writes a file to disk."""
    data = pd.DataFrame(
        {
            "datetime": pd.date_range("2023-01-01", periods=5, freq="D"),
            "temperature_celsius": [1.0, 2.0, 3.0, 4.0, 5.0],
        }
    )

    fig = plot_temperature_over_time(data)
    output_path = tmp_path / "plot.png"

    save_plot(fig, output_path)

    assert output_path.exists()
