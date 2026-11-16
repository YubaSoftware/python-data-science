import unittest

from code.descriptive_stats import data_range, mean, median, modes, standard_deviation, variance


class BasicStatisticsTests(unittest.TestCase):
    def test_mean_returns_average(self):
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_mean_rejects_empty_sequence(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_median_handles_odd_and_even_sequences(self):
        self.assertEqual(median([9, 1, 5]), 5)
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_median_rejects_empty_sequence(self):
        with self.assertRaises(ValueError):
            median([])

    def test_modes_returns_all_tied_values(self):
        self.assertEqual(modes([1, 1, 2, 2, 3]), [1, 2])

    def test_range_and_variance(self):
        self.assertEqual(data_range([1, 2, 3]), 2)
        self.assertAlmostEqual(variance([1, 2, 3]), 2 / 3)
        self.assertEqual(variance([1, 2, 3], sample=True), 1)
        self.assertAlmostEqual(standard_deviation([1, 2, 3]), (2 / 3) ** 0.5)

    def test_sample_variance_requires_two_values(self):
        with self.assertRaises(ValueError):
            variance([1], sample=True)


if __name__ == "__main__":
    unittest.main()
