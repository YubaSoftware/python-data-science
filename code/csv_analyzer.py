"""Summarize columns in a CSV file and print a JSON report."""

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any


def analyze_csv(path: str | Path) -> dict[str, Any]:
    """Return row counts, missing-value counts, and numeric summaries by column."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        headers = reader.fieldnames
        if not headers:
            raise ValueError("CSV file must have a header row")
        if any(not header.strip() for header in headers):
            raise ValueError("CSV column names cannot be empty")
        if len(set(headers)) != len(headers):
            raise ValueError("CSV column names must be unique")

        columns = {
            header: {"missing": 0, "non_numeric": 0, "numeric_values": []}
            for header in headers
        }
        row_count = 0
        for row in reader:
            if None in row:
                raise ValueError(f"row {row_count + 2} has more fields than the header")
            row_count += 1
            for header in headers:
                value = row.get(header)
                if value is None or not value.strip():
                    columns[header]["missing"] += 1
                    continue
                try:
                    number = float(value)
                except ValueError:
                    columns[header]["non_numeric"] += 1
                    continue
                if math.isfinite(number):
                    columns[header]["numeric_values"].append(number)
                else:
                    columns[header]["non_numeric"] += 1

    summaries: dict[str, Any] = {}
    for header, column in columns.items():
        numbers = column.pop("numeric_values")
        summary: dict[str, Any] = {
            "missing": column["missing"],
            "non_numeric": column["non_numeric"],
            "numeric_count": len(numbers),
        }
        if numbers:
            summary.update(
                minimum=min(numbers),
                maximum=max(numbers),
                mean=sum(numbers) / len(numbers),
            )
        summaries[header] = summary
    return {"rows": row_count, "columns": summaries}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="path to the CSV file")
    args = parser.parse_args()
    try:
        report = analyze_csv(args.csv_file)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
