# Choosing a data visualization

Start with the question and data types, then choose the simplest chart that answers it:

- **Line:** change over ordered time or another continuous sequence.
- **Bar:** compare values across categories.
- **Scatter:** examine the relationship between two numeric variables.
- **Histogram:** show the distribution of one numeric variable.
- **Box plot:** compare a distribution's center, spread, and potential outliers.
- **Heatmap:** show a matrix of values, often correlations.

Avoid implying a continuous trend with unordered categories. Label units, show meaningful scales, and distinguish association from causation. The current [CSV plotting tool](../visualizations/plot_csv.py) implements the first four chart types.
