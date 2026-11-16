import csv
import tempfile
import unittest
from pathlib import Path

from code.csv_analyzer import analyze_csv
from code.data_cleaner import clean_csv
from code.dataset_generator import generate_samples_csv


class CsvAnalyzerTests(unittest.TestCase):
    def test_reports_missing_and_numeric_values(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text("label,value\none,2\n two ,\nthree,4\n", encoding="utf-8")

            report = analyze_csv(path)

        self.assertEqual(report["rows"], 3)
        self.assertEqual(report["columns"]["value"]["missing"], 1)
        self.assertEqual(report["columns"]["value"]["numeric_count"], 2)
        self.assertEqual(report["columns"]["value"]["mean"], 3)
        self.assertEqual(report["columns"]["label"]["non_numeric"], 3)

    def test_rejects_duplicate_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text("value,value\n1,2\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "unique"):
                analyze_csv(path)


class CsvCleanerTests(unittest.TestCase):
    def test_drops_requested_rows_and_preserves_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.csv"
            output = Path(directory) / "clean.csv"
            original = "name,value\nA,1\nA,1\nB,\nC,3\n"
            source.write_text(original, encoding="utf-8")

            report = clean_csv(source, output, drop_duplicates=True, drop_incomplete=True)

            self.assertEqual(source.read_text(encoding="utf-8"), original)
            with output.open(encoding="utf-8", newline="") as file:
                rows = list(csv.reader(file))

        self.assertEqual(rows, [["name", "value"], ["A", "1"], ["C", "3"]])
        self.assertEqual(report["incomplete_rows_removed"], 1)
        self.assertEqual(report["duplicate_rows_removed"], 1)

    def test_refuses_to_overwrite_input_or_output(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.csv"
            existing_output = Path(directory) / "existing.csv"
            source.write_text("name\nA\n", encoding="utf-8")
            existing_output.write_text("preserve me\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "different file"):
                clean_csv(source, source, drop_duplicates=True)
            with self.assertRaises(FileExistsError):
                clean_csv(source, existing_output, drop_duplicates=True)
            self.assertEqual(existing_output.read_text(encoding="utf-8"), "preserve me\n")


class DatasetGeneratorTests(unittest.TestCase):
    def test_generates_repeatable_data_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.csv"
            second = Path(directory) / "second.csv"
            generate_samples_csv(first, count=3, seed=7)
            generate_samples_csv(second, count=3, seed=7)

            self.assertEqual(first.read_text(encoding="utf-8"), second.read_text(encoding="utf-8"))
            with self.assertRaises(FileExistsError):
                generate_samples_csv(first, count=1)


if __name__ == "__main__":
    unittest.main()
