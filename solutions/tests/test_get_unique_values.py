import csv
import os
import unittest

from solutions.get_unique_values import get_unique_values


class TestGetUniqueValues(unittest.TestCase):
    """Tests for the get_unique_values function."""

    def setUp(self):
        """Create a sample CSV file for testing."""
        with open("test_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["col1", "col2"])
            writer.writerows([[1, "a"], [2, "b"], [2, "a"], [3, "c"]])

    def tearDown(self):
        """Remove the sample CSV file after testing."""
        os.remove("test_data.csv")

    def test_empty_file(self):
        """Test with an empty file (with header)."""
        with open("empty_file.csv", "w") as f:
            f.write("col1,col2\n")
        self.assertEqual(get_unique_values("empty_file.csv", "col1"), [])
        os.remove("empty_file.csv")

    def test_unique_values_col1(self):
        """Test unique values extraction from col1."""
        self.assertEqual(
            set(get_unique_values("test_data.csv", "col1")), {str(1), str(2), str(3)}
        )

    def test_unique_values_col2(self):
        """Test unique values extraction from col2."""
        self.assertEqual(
            set(get_unique_values("test_data.csv", "col2")), {"a", "b", "c"}
        )

    def test_file_not_found(self):
        """Test with a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            get_unique_values("nonexistent_file.csv", "col1")

    def test_column_not_in_csv(self):
        """Test with a column not in the CSV."""
        with self.assertRaises(KeyError):
            get_unique_values("test_data.csv", "non_existent_column")
