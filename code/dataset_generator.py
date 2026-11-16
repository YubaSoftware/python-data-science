"""Generate a small, reproducible synthetic CSV dataset."""

import argparse
import csv
import random
from pathlib import Path


def generate_samples_csv(path: str | Path, count: int = 20, seed: int = 0) -> None:
    """Create sample_id, value, and group columns without overwriting a file."""
    if count < 0:
        raise ValueError("count must be zero or greater")

    generator = random.Random(seed)
    with Path(path).open("x", encoding="utf-8", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["sample_id", "value", "group"])
        for sample_id in range(1, count + 1):
            writer.writerow([sample_id, round(generator.uniform(0, 100), 2), generator.choice(["A", "B", "C"])])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    try:
        generate_samples_csv(args.output_csv, args.count, args.seed)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
