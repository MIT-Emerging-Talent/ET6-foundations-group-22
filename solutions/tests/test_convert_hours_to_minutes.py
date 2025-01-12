#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the convert_hours_to_minutes function.

Test cases include:
    - Valid inputs for standard calculations
    - Boundary cases
    - Defensive tests for invalid inputs

Created on 2024-12-31
Author: Azza
"""

import unittest

from solutions.convert_hours_to_minutes import convert_hours_to_minutes


class TestConvertHoursToMinutes(unittest.TestCase):
    """Unit tests for the convert_hours_to_minutes function."""

    def test_one_hour(self):
        """It should return 60 minutes for 1 hour."""
        self.assertEqual(convert_hours_to_minutes(1), 60)

    def test_multiple_hours(self):
        """It should return 300 minutes for 5 hours."""
        self.assertEqual(convert_hours_to_minutes(5), 300)

    def test_zero_hours(self):
        """It should return 0 minutes for 0 hours."""
        self.assertEqual(convert_hours_to_minutes(0), 0)

    def test_large_number_of_hours(self):
        """It should return 60000 minutes for 1000 hours."""
        self.assertEqual(convert_hours_to_minutes(1000), 60000)

    def test_negative_hours(self):
        """It should raise an AssertionError for negative hours."""
        with self.assertRaises(AssertionError):
            convert_hours_to_minutes(-5)

    def test_string_input(self):
        """It should raise an AssertionError for string input."""
        with self.assertRaises(AssertionError):
            convert_hours_to_minutes("3")

    def test_float_input(self):
        """It should raise an AssertionError for float input."""
        with self.assertRaises(AssertionError):
            convert_hours_to_minutes(2.5)

    def test_none_input(self):
        """It should raise an AssertionError for None input."""
        with self.assertRaises(AssertionError):
            convert_hours_to_minutes(None)

    def test_list_input(self):
        """It should raise an AssertionError for list input."""
        with self.assertRaises(AssertionError):
            convert_hours_to_minutes([1, 2])


if __name__ == "__main__":
    unittest.main()
