# Data cleaning

Cleaning makes assumptions about what counts as incomplete, invalid, or duplicated. Inspect the data and choose a rule before changing it; preserve the original source.

The [`csv_analyzer.py`](../code/csv_analyzer.py) tool reports missing and non-numeric cells. [`data_cleaner.py`](../code/data_cleaner.py) writes a separate output file and only removes rows when requested:

```powershell
py -3 code\data_cleaner.py input.csv output.csv --drop-incomplete --drop-duplicates
```

Here, an incomplete row has at least one blank field, and a duplicate is an exact repeated row. The first copy is kept. The tool refuses to overwrite an existing output or the input file. Review its counts and inspect the cleaned output before using it.
