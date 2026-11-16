"""A small runnable demonstration of the descriptive statistics helpers."""

if __package__:
    from .descriptive_stats import mean, median
else:
    from descriptive_stats import mean, median


if __name__ == "__main__":
    daily_temperatures = [18, 21, 19, 23, 20]
    print(f"Mean temperature: {mean(daily_temperatures):.1f}")
    print(f"Median temperature: {median(daily_temperatures):.1f}")
