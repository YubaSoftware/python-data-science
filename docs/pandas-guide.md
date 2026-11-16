# pandas guide

pandas provides labeled `Series` and table-shaped `DataFrame` objects. It is especially useful for filtering, grouping, joining, and cleaning tabular data.

```python
import pandas as pd

weather = pd.read_csv("datasets/weather.csv")
print(weather.head())
print(weather.groupby("date")["temperature"].mean())
```

Useful first steps include `read_csv`, inspecting `head()` and `dtypes`, selecting columns, boolean filtering, `groupby`, `isna`, `drop_duplicates`, and writing results with `to_csv`. Make cleaning decisions explicit and keep the raw input unchanged.

Install it with `py -m pip install pandas`. The standard-library [`csv_analyzer.py`](../code/csv_analyzer.py) offers a small no-dependency alternative.
