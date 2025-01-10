"""
Unit tests for the check_number_type function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions


Created on 05 01 2025
@author: Eman Alfalouji
"""

import unittest

from solutions.check_number_type import check_number_type


class TestCheckNumberType(unittest.TestCase):
    """Tests the check_number_type function."""

    def test_even_number(self):
        """It should identify even numbers."""
        self.assertEqual(check_number_type("22"), "The number is even")

    def test_odd_number(self):
        """It should identify odd numbers."""
        self.assertEqual(check_number_type("15"), "The number is odd")

    def test_zero(self):
        """It should identify zero as even."""
        self.assertEqual(check_number_type("0"), "The number is even")

    def test_negative_even_number(self):
        """It should identify negative even numbers."""
        self.assertEqual(check_number_type("-4"), "The number is even")

    def test_negative_odd_number(self):
        """It should identify negative odd numbers."""
        self.assertEqual(check_number_type("-7"), "The number is odd")

    def test_input_with_whitespace(self):
        """It should handle inputs with leading/trailing whitespace."""
        self.assertEqual(check_number_type("   8   "), "The number is even")

    def test_invalid_input(self):
        """It should raise ValueError for invalid inputs."""
        with self.assertRaises(ValueError):
            check_number_type("abc")

    def test_empty_input(self):
        """It should raise ValueError for empty inputs."""
        with self.assertRaises(ValueError):
            check_number_type("")


if __name__ == "__main__":
    unittest.main()
