# Data formats

- **CSV:** plain-text rows and columns; easy to inspect and supported by spreadsheets. It has limited type and metadata support.
- **JSON:** nested objects and arrays; useful for structured records and web APIs.
- **XLSX:** spreadsheet workbook format with multiple sheets and formatting; Python libraries such as `openpyxl` can read and write it.
- **Parquet:** compressed, column-oriented format suited to larger analytical tables; commonly used through `pyarrow` or pandas.
- **SQLite:** a self-contained relational database file queried with SQL; Python includes the `sqlite3` module.
- **IPYNB:** a notebook document containing code, explanatory text, and optional output.

Choose a format based on size, structure, interoperability, and whether formatting or multiple sheets matter. Small examples here use CSV; install optional readers only when a project needs them.
