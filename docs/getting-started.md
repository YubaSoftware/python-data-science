# Getting started

## Install Python

Install Python 3.10 or later from [python.org](https://www.python.org/downloads/). On Windows, the Python launcher is usually `py`; on macOS and Linux, use `python3` in the commands below.

## Create an environment

From the repository root, create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the charting dependency:

```powershell
py -m pip install -r requirements.txt
```

The CSV and statistics examples use only the standard library. NumPy, pandas, Jupyter, and spreadsheet readers are optional; install them when following the corresponding guide.

## Try the examples

```powershell
py -3 code\csv_analyzer.py datasets\weather.csv
py -3 code\basic_statistics.py
py -3 -m unittest discover -s tests
```

To explore the notebook, install Jupyter with `py -m pip install jupyterlab`, then run `jupyter lab` from the repository root.
