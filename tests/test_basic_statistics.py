import unittest

from code.basic_statistics import mean, median


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


if __name__ == "__main__":
    unittest.main()
