"""Write a cleaned CSV copy using explicitly selected cleaning rules."""

import argparse
import csv
from pathlib import Path


def clean_csv(
    source_path: str | Path,
    output_path: str | Path,
    *,
    drop_duplicates: bool = False,
    drop_incomplete: bool = False,
) -> dict[str, int]:
    """Write a new CSV, optionally dropping duplicate or incomplete rows."""
    source = Path(source_path).resolve()
    output = Path(output_path).resolve()
    if source == output:
        raise ValueError("output must be a different file from the input")

    with source.open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.reader(input_file)
        try:
            header = next(reader)
        except StopIteration as error:
            raise ValueError("CSV file must have a header row") from error
        if not header or any(not name.strip() for name in header):
            raise ValueError("CSV column names cannot be empty")
        if len(set(header)) != len(header):
            raise ValueError("CSV column names must be unique")

        rows: list[list[str]] = []
        seen: set[tuple[str, ...]] = set()
        input_rows = incomplete_rows = duplicate_rows = 0
        for line_number, row in enumerate(reader, start=2):
            input_rows += 1
            if len(row) != len(header):
                raise ValueError(f"row {line_number} has a different number of fields than the header")
            if drop_incomplete and any(not value.strip() for value in row):
                incomplete_rows += 1
                continue
            key = tuple(row)
            if drop_duplicates and key in seen:
                duplicate_rows += 1
                continue
            seen.add(key)
            rows.append(row)

    with output.open("x", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(rows)

    return {
        "input_rows": input_rows,
        "output_rows": len(rows),
        "incomplete_rows_removed": incomplete_rows,
        "duplicate_rows_removed": duplicate_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("--drop-duplicates", action="store_true", help="keep only the first exact copy of each row")
    parser.add_argument("--drop-incomplete", action="store_true", help="remove rows with an empty field")
    args = parser.parse_args()
    if not args.drop_duplicates and not args.drop_incomplete:
        parser.error("select at least one cleaning rule")
    try:
        report = clean_csv(
            args.input_csv,
            args.output_csv,
            drop_duplicates=args.drop_duplicates,
            drop_incomplete=args.drop_incomplete,
        )
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.error(str(error))
    print(report)


if __name__ == "__main__":
    main()
