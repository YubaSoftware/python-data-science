# Visualizations

[`plot_csv.py`](plot_csv.py) creates line, bar, scatter, and histogram charts from CSV columns using Matplotlib.

```powershell
py -3 visualizations\plot_csv.py datasets\weather.csv --kind line --x date --y temperature --output visualizations\output\weather.png
py -3 visualizations\plot_csv.py datasets\weather.csv --kind hist --y temperature --output visualizations\output\temperature.svg
```

Generated files should be treated as analysis outputs and are ignored under `visualizations/output/`. Use `--help` to see the available options.
