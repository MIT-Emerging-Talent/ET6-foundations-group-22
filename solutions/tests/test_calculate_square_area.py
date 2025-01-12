# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for square_area function.

Test categories:
- Standard cases: positive numbers
- Edge cases: numbers that are positive but less than 1
- Defensive cases: wrong input types, value that is zero, and less than zero

Created on 07 01 2024
Author: Kareiman Altayeb
"""

import unittest

from solutions.calculate_square_area import calculate_square_area


class CalculateSquareArea(unittest.TestCase):
    """Tests the calculate_square_area function"""

    def test_positive_integers(self):
        """It should return value ^ 2"""
        self.assertEqual(calculate_square_area(7), 49)

    def test_positive_float(self):
        """It should return value ^ 2"""
        self.assertEqual(calculate_square_area(5.5), 30.25)

    def test_bigger_values(self):
        """It should return the value ^ 2"""
        self.assertEqual(calculate_square_area(2222), 4937284)

    # Edge cases

    def test_small_values(self):
        """It should return the value ^ 2"""
        self.assertEqual(calculate_square_area(0.75), 0.5625)

    # Defensive cases

    def test_string_entry(self):
        """It should raise AssertionError if entry was text or letters"""
        with self.assertRaises(AssertionError):
            calculate_square_area("a")

    def test_value_zero(self):
        """It should raise AssertionError if entry was zero"""
        with self.assertRaises(AssertionError):
            calculate_square_area(0)

    def test_value_negative(self):
        """It should raise AssertionError if value was less than zero"""
        with self.assertRaises(AssertionError):
            calculate_square_area(-3)

    if __name__ == "__main__":
        unittest.main()
