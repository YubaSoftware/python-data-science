# Python for data science

Python programs combine values, collections, decisions, loops, and functions. Data work often starts with lists of measurements and dictionaries representing table rows.

```python
temperatures = [16.2, 17.8, 15.4]
warm_days = [value for value in temperatures if value >= 17]
print(warm_days)
```

Use functions to give repeatable operations a name, and use `csv.DictReader` to read rows with named columns. The examples in [`code/`](../code/) use type hints, functions, and explicit error handling. Practice with [`weather.csv`](../datasets/weather.csv).

Before reaching for a library, become comfortable with numbers, strings, lists, dictionaries, loops, functions, imports, and reading error messages.
