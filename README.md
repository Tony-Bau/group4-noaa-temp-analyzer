# noaa-temp-analyzer

A command-line tool for downloading, analyzing, and visualizing NOAA ISD-Lite weather data.

---

## Description

This project was developed by **Group 4** as part of the **Research Software Engineering (RSE) Lab** course.

The application allows users to download NOAA ISD-Lite weather data for a selected weather station and year, clean temperature measurements, calculate summary statistics, and optionally generate and save temperature-over-time plots.

The project follows a modular design with separate components for downloading, loading, cleaning, analyzing, and visualizing weather data.

---

## Features

- Download NOAA ISD-Lite weather data for a selected weather station and year.
- Load and parse compressed NOAA ISD-Lite weather files.
- Clean temperature measurements by:
  - removing invalid values,
  - handling missing data,
  - converting temperatures from tenths of a degree to degrees Celsius.
- Calculate summary statistics including:
  - Number of valid measurements
  - Mean temperature
  - Minimum temperature
  - Maximum temperature
  - Median temperature
  - Standard deviation
- Generate and save temperature-over-time plots.
- Support terminal-only output using `--text-only`.
- Support configurable logging levels using:
  - `-v`
  - `-vv`
  - `-vvv`

---

## Installation

### Prerequisites

- Python 3.10
- uv

Clone the repository:

```bash
git clone <repository-url>
cd group-4
```

Install all project dependencies:

```bash
uv sync
```

---

## Requirements

### Runtime Dependencies

- pandas
- matplotlib
- click
- requests

### Development Dependencies

- pytest
- ruff

---

## Usage

### Basic Example

```bash
uv run noaa-temp-analyzer \
    --station 010010-99999 \
    --year 2020
```

### Text-Only Mode

```bash
uv run noaa-temp-analyzer \
    --station 010010-99999 \
    --year 2020 \
    --text-only
```

### Verbose Output

```bash
uv run noaa-temp-analyzer \
    --station 010010-99999 \
    --year 2020 \
    -vv
```

---

## Workflow

The application performs the following steps:

1. Download the NOAA ISD-Lite weather data.
2. Load and parse the downloaded dataset.
3. Clean the temperature measurements.
4. Calculate summary statistics.
5. Print the analysis results.
6. Optionally generate and save a temperature plot.

---

## Output Files

During execution, the application creates the following directories:

- `data/` – stores downloaded NOAA ISD-Lite weather data.
- `plots/` – stores generated temperature plots when `--text-only` is **not** enabled.

These files are generated locally and should not be committed to the repository.

---

## Project Structure

```text
src/
└── noaa_temp_analyzer/
    ├── __main__.py
    ├── cli.py
    ├── downloader.py
    ├── loader.py
    ├── cleaner.py
    ├── analysis.py
    └── plotting.py

tests/
├── test_cli.py
├── test_downloader.py
├── test_loader.py
├── test_cleaner.py
└── test_analysis.py
```

### Module Overview

| Module | Responsibility |
|---------|----------------|
| `cli.py` | Command-line interface |
| `downloader.py` | Download NOAA ISD-Lite weather data |
| `loader.py` | Load and parse weather data |
| `cleaner.py` | Clean temperature measurements |
| `analysis.py` | Calculate summary statistics |
| `plotting.py` | Generate and save temperature plots |

---

## Example Output

```text
Temperature statistics

Valid measurements: 8653
Mean temperature: 0.41 °C
Minimum temperature: -14.1 °C
Maximum temperature: 10.7 °C
Median temperature: 1.0 °C
Standard deviation: 4.43 °C
```

When graphics are enabled, the generated plot is saved to the `plots/` directory.

---

## Testing & CI

The project uses GitLab CI together with **pytest** and **Ruff** to maintain code quality.

### Run Tests

```bash
uv run pytest
```

### Run Ruff Checks

```bash
uv run ruff check .
```

### Verify Formatting

```bash
uv run ruff format --check .
```

### Automatically Format the Code

```bash
uv run ruff format .
```

### CLI Smoke Test

The CI pipeline also performs a simple smoke test to verify that the command-line interface runs successfully.

```bash
uv run noaa-temp-analyzer \
    --station 010030-99999 \
    --year 2025 \
    --text-only
```

---

## Contributing

Please refer to **CONTRIBUTING.md** for details on:

- GitLab workflow
- Branch naming conventions
- Merge Request process
- Commit message conventions
- Code quality requirements

---

## Citation

If you use this software in research or teaching, please cite the project using the metadata provided in **CITATION.cff**.

---

## Authors

Developed by **Group 4**:

- Yusuf Bildik
- Friedrich Vincent Löwe
- Prem Murugaraj
- Tony Baudis

---

## License

This project is licensed under the **MIT License**. See **LICENSE.md** for details.