# noaa-temp-analyzer

A command-line tool for analyzing NOAA ISD-Lite weather data.

## Description

This project was developed by **Group 4** as part of the **RSE Lab** course.

The tool allows users to select a weather station and a year, load the corresponding NOAA ISD-Lite weather data, clean temperature measurements, and generate a concise analysis. Optionally, the application can create visualizations and either display them interactively or save them for later use.

---

## Features

* **Station Selection** – Specify a weather station using:

  ```bash
  --station <station_id>
  ```

* **Year Selection** – Select the year to analyze:

  ```bash
  --year <year>
  ```

* **Verbose Logging** – Control logging detail levels:

  ```bash
  -v
  -vv
  -vvv
  ```

* **Text-Only Mode** – Print analysis results directly to the terminal:

  ```bash
  --text-only
  ```

* **Data Visualization** – Generate and display or save temperature plots.

---

## Installation & Setup

This project uses **uv** for dependency and environment management.

### Prerequisites

* Python 3.10

### Install Dependencies

```bash
uv sync
```

---

## Requirements

### Core Dependencies

* pandas
* matplotlib
* click

### Development Tools (defined in dependency-groups)

* ruff
* pytest

---

## Usage

> **Temporary Note:** The usage examples below use `uv run python main.py`. later we'll update this to the final CLI command.
### Basic Example

```bash
uv run python main.py --station 10468099999 --year 2023
```

### Text-Only Mode

```bash
uv run python main.py --station 10468099999 --year 2023 --text-only
```

### Verbose Output

```bash
uv run python main.py --station 10468099999 --year 2023 -vv
```

---

## Testing & CI

We use GitLab's built-in Continuous Integration (CI) to ensure code stability and maintain code quality.

### Automated Checks

* **Automated Testing:** Every Merge Request triggers a GitLab CI pipeline that runs the test suite using `pytest`.
* **Code Quality:** The pipeline also performs linting and formatting checks using `ruff`.

### Run Tests Locally

Before pushing your changes, run:

```bash
uv run pytest
```

### Run Linting Locally

```bash
uv run ruff check .
```

---

## Contributing

Please refer to **CONTRIBUTING.md** for details about:

* GitLab workflow
* Branch naming conventions
* Merge Request process
* Commit message style
* Code quality requirements

---

## Authors

Developed by **Group 4**:

* Yusuf Bildik
* Friedrich Vincent Löwe
* Prem Murugaraj
* Tony Baudis

---

## License

This project is licensed under the **MIT License**. See the `LICENSE.md` file for details.
