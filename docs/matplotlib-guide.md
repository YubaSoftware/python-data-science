# Matplotlib guide

Matplotlib creates static charts suitable for notebooks, reports, and documentation. This repository's [`plot_csv.py`](../visualizations/plot_csv.py) supports line, bar, scatter, and histogram plots from CSV columns.

```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed"]
values = [16, 18, 17]
plt.plot(days, values, marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.show()
```

Add a descriptive title and axis labels, choose a chart that matches the question, and avoid decoration that obscures the data. Install Matplotlib with `py -m pip install -r requirements.txt`.
