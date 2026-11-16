"""Descriptive statistics implemented with the Python standard library."""

from collections import Counter
from collections.abc import Sequence
from math import sqrt


def _require_values(values: Sequence[float]) -> None:
    if not values:
        raise ValueError("at least one value is required")


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence."""
    _require_values(values)
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the middle value, or the average of the two middle values."""
    _require_values(values)
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def modes(values: Sequence[float]) -> list[float]:
    """Return all values tied for the highest frequency."""
    _require_values(values)
    counts = Counter(values)
    highest_frequency = max(counts.values())
    return [value for value, frequency in counts.items() if frequency == highest_frequency]


def data_range(values: Sequence[float]) -> float:
    """Return the difference between the largest and smallest values."""
    _require_values(values)
    return max(values) - min(values)


def variance(values: Sequence[float], *, sample: bool = False) -> float:
    """Return population variance, or sample variance when sample=True."""
    _require_values(values)
    if sample and len(values) < 2:
        raise ValueError("sample variance requires at least two values")

    center = mean(values)
    divisor = len(values) - 1 if sample else len(values)
    return sum((value - center) ** 2 for value in values) / divisor


def standard_deviation(values: Sequence[float], *, sample: bool = False) -> float:
    """Return the square root of the population or sample variance."""
    return sqrt(variance(values, sample=sample))


if __name__ == "__main__":
    example_values = [18, 21, 19, 23, 20]
    print(f"Mean: {mean(example_values):.2f}")
    print(f"Median: {median(example_values):.2f}")
    print(f"Range: {data_range(example_values):.2f}")
    print(f"Population standard deviation: {standard_deviation(example_values):.2f}")
