"""Create temperature plots."""

import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


LOGGER = logging.getLogger(__name__)


def plot_temperature_over_time(
    data: pd.DataFrame,
    title: str = "Temperature over time",
) -> Figure:
    """Create a line plot of temperature over time."""
    required_columns = {"datetime", "temperature_celsius"}

    if not required_columns.issubset(data.columns):
        raise ValueError(
            "Data must contain 'datetime' and 'temperature_celsius' columns."
        )

    LOGGER.info("Creating temperature plot.")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(data["datetime"], data["temperature_celsius"])
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature [°C]")
    ax.grid(True)

    fig.autofmt_xdate()
    fig.tight_layout()

    return fig


def save_plot(fig: Figure, output_path: str | Path) -> None:
    """Save a plot to a file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(output_path, dpi=300)

    LOGGER.info("Saved plot to: %s", output_path)
