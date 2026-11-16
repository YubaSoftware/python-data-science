# Statistics

Descriptive statistics summarize observed values; they do not by themselves explain causes or prove that a pattern will continue.

- **Mean:** sum divided by count; sensitive to extreme values.
- **Median:** middle sorted value, or the average of the two middle values; more resistant to extremes.
- **Mode:** most frequent value; there can be ties or no uniquely useful mode.
- **Range:** maximum minus minimum.
- **Variance:** average squared distance from the mean. Population variance divides by `n`; sample variance divides by `n - 1`.
- **Standard deviation:** square root of variance, expressed in the original unit.

The reusable functions are in [`code/descriptive_stats.py`](../code/descriptive_stats.py). The `variance` and `standard_deviation` helpers default to population formulas; pass `sample=True` for sample formulas. Empty inputs raise `ValueError`.
