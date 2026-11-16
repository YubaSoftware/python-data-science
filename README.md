# Python Data Science

A beginner-friendly learning and experimentation repository for Python, data analysis, statistics, and visualization. Examples use small synthetic datasets; core tools use the Python standard library, with Matplotlib used for charts.

## Get started

Use Python 3.10 or later. From PowerShell, create an environment and install the optional charting dependency:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Run the CSV summary tool:

```powershell
py -3 code\csv_analyzer.py datasets\weather.csv
```

Create a chart (requires the dependencies in `requirements.txt`):

```powershell
py -3 visualizations\plot_csv.py datasets\weather.csv --kind line --x date --y temperature --output visualizations\output\weather.png
```

Run the test suite:

```powershell
py -3 -m unittest discover -s tests
```

## Repository map

```text
code/             Reusable statistics and CSV tools
data/raw/         Place for original, local datasets
data/processed/   Place for cleaned, derived datasets
datasets/         Small, synthetic, version-controlled examples
docs/             Short guides, glossary, and references
notebooks/        Exploratory Jupyter notebooks
tests/            Standard-library unit tests
visualizations/   Charting tools and generated output
```

Start with the [documentation index](docs/README.md), then explore the [weather analysis notebook](notebooks/01-weather-analysis.ipynb). The datasets are synthetic and intended for practice, not as factual references.
