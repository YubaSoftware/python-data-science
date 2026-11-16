"""A few basic descriptive statistics, implemented with the Python standard library."""

from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the middle value of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("median requires at least one value")

    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


if __name__ == "__main__":
    daily_temperatures = [18, 21, 19, 23, 20]
    print(f"Mean temperature: {mean(daily_temperatures):.1f}")
    print(f"Median temperature: {median(daily_temperatures):.1f}")
