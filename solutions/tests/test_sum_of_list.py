"""
Unit tests for the sum_of_list function.

Test categories:
    - Standard cases: typical lists with positive, negative, and mixed numbers
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, invalid elements

Created on 05 01 2025
@author: Eman Alfalouji
"""

import unittest

from solutions.sum_of_list import sum_of_list


class TestSumOfList(unittest.TestCase):
    """Tests the sum_of_list function."""

    # Standard test cases
    def test_positive_numbers(self):
        """Test that the function correctly sums a list of positive integers."""
        self.assertEqual(sum_of_list([8, 7, 3, 4, 5]), 27)

    def test_negative_numbers(self):
        """Test that the function correctly sums a list of negative integers."""
        self.assertEqual(sum_of_list([-1, -4, -7]), -12)

    def test_mixed_numbers(self):
        """
        Test that the function correctly sums a list with both positive and negative numbers,
        including floats.
        """
        self.assertEqual(sum_of_list([1, -2, 3.5]), 2.5)

    # Edge cases
    def test_empty_list(self):
        """Test that the function returns 0 for an empty list."""
        self.assertEqual(sum_of_list([]), 0)

    def test_single_element(self):
        """Test that the function returns the single element value when the list has only one number."""
        self.assertEqual(sum_of_list([10]), 10)

    # Defensive cases
    def test_invalid_input_type(self):
        """Test that the function raises a TypeError when the input is not a list."""
        with self.assertRaises(TypeError):
            sum_of_list("not a list")

    def test_invalid_element_type(self):
        """Test that the function raises a ValueError when the list contains non-numeric elements."""
        with self.assertRaises(ValueError):
            sum_of_list([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
