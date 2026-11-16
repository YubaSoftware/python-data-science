"""Create a basic chart from columns in a CSV file."""

import argparse
import csv
import math
from pathlib import Path


def _read_columns(path: Path, names: list[str]) -> dict[str, list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise ValueError("CSV file must have a header row")
        if any(not name.strip() for name in reader.fieldnames):
            raise ValueError("CSV column names cannot be empty")
        if len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("CSV column names must be unique")
        if any(name not in reader.fieldnames for name in names):
            raise ValueError(f"requested columns not found; available: {', '.join(reader.fieldnames)}")
        columns = {name: [] for name in names}
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"row {line_number} has more fields than the header")
            for name in names:
                value = row.get(name)
                if value is None or not value.strip():
                    raise ValueError(f"row {line_number} has an empty value in {name!r}")
                columns[name].append(value)
    if not columns or not next(iter(columns.values())):
        raise ValueError("CSV file has no data rows")
    return columns


def plot_csv(
    csv_path: str | Path,
    *,
    kind: str,
    output_path: str | Path,
    x_column: str | None = None,
    y_column: str,
    bins: int = 10,
) -> None:
    """Create and save a chart; histogram uses only y_column."""
    if kind not in {"line", "bar", "scatter", "hist"}:
        raise ValueError("kind must be line, bar, scatter, or hist")
    if bins < 1:
        raise ValueError("bins must be at least one")

    output = Path(output_path)
    if output.suffix.lower() not in {".png", ".svg"}:
        raise ValueError("output file must have a .png or .svg extension")
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")

    if kind == "hist":
        columns = _read_columns(Path(csv_path), [y_column])
    else:
        if x_column is None:
            raise ValueError(f"{kind} charts require both --x and --y columns")
        columns = _read_columns(Path(csv_path), [x_column, y_column])
    try:
        y_values = [float(value) for value in columns[y_column]]
        if not all(math.isfinite(value) for value in y_values):
            raise ValueError(f"column {y_column!r} contains a non-finite number")
        if kind == "scatter":
            x_values: list[str] | list[float] = [float(value) for value in columns[x_column]]
            if not all(math.isfinite(value) for value in x_values):
                raise ValueError(f"column {x_column!r} contains a non-finite number")
        elif kind != "hist":
            x_values = columns[x_column]
    except ValueError as error:
        if str(error).startswith("column "):
            raise
        raise ValueError("plotted numeric columns must contain only numbers") from error

    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as error:
        if error.name == "matplotlib":
            raise ModuleNotFoundError(
                "Matplotlib is required; install it with `py -m pip install -r requirements.txt`"
            ) from error
        raise

    figure, axes = plt.subplots()
    if kind == "line":
        axes.plot(x_values, y_values, marker="o")
        axes.set_xlabel(x_column)
    elif kind == "bar":
        axes.bar(x_values, y_values)
        axes.set_xlabel(x_column)
    elif kind == "scatter":
        axes.scatter(x_values, y_values)
        axes.set_xlabel(x_column)
    else:
        axes.hist(y_values, bins=bins)
    axes.set_ylabel(y_column)
    axes.set_title(f"{kind.title()} of {y_column}")
    figure.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output)
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--kind", choices=("line", "bar", "scatter", "hist"), required=True)
    parser.add_argument("--x", dest="x_column", help="category/time or numeric x column; not used for histograms")
    parser.add_argument("--y", dest="y_column", required=True, help="numeric y column")
    parser.add_argument("--bins", type=int, default=10, help="histogram bin count")
    parser.add_argument("--output", type=Path, required=True, help="new .png or .svg output path")
    args = parser.parse_args()
    try:
        plot_csv(
            args.csv_file,
            kind=args.kind,
            x_column=args.x_column,
            y_column=args.y_column,
            bins=args.bins,
            output_path=args.output,
        )
    except (OSError, UnicodeError, csv.Error, ValueError, ModuleNotFoundError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
