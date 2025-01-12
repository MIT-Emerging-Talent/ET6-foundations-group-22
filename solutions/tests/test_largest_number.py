#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the largest_number function.

Test categories:
Standard cases: Typical lists with positive, negative, and mixed integers.
Edge cases: Empty lists, lists with a single element, lists with duplicate values.
Defensive tests: Non-list inputs (e.g., integers, strings), lists with non-integer elements,
assertions for invalid inputs.

Created on 2025-01-11
Author: Azza
"""

import unittest

from ..largest_number import largest_number


class TestLargestNumber(unittest.TestCase):
    """Unit tests for the largest_number function."""

    def test_standard_list(self):
        """It should return 9 for [0, 1, 9, 2, 6, 4]."""
        self.assertEqual(largest_number([0, 1, 9, 2, 6, 4]), 9)

    def test_single_element(self):
        """It should return 12 for [12]."""
        self.assertEqual(largest_number([12]), 12)

    def test_mixed_positive_and_negative(self):
        """It should return 8 for [8, -1, -8, 5]."""
        self.assertEqual(largest_number([8, -1, -8, 5]), 8)

    def test_all_negative_numbers(self):
        """It should return -1 for [-9, -1, -6, -5]."""
        self.assertEqual(largest_number([-9, -1, -6, -5]), -1)

    def test_all_zeros(self):
        """It should return 0 for [0, 0]."""
        self.assertEqual(largest_number([0, 0]), 0)

    def test_large_numbers(self):
        """It should return 4294967296 for [2**32, 2**16, 2**8, 1]."""
        self.assertEqual(largest_number([2**32, 2**16, 2**8, 1]), 2**32)

    def test_empty_list(self):
        """It should raise ValueError for an empty list."""
        with self.assertRaises(ValueError):
            largest_number([])

    def test_non_list_input(self):
        """It should raise TypeError for non-list input, e.g., 42."""
        with self.assertRaises(TypeError):
            largest_number(42)

    def test_list_with_non_integer(self):
        """It should raise TypeError for a list with non-integer elements."""
        with self.assertRaises(TypeError):
            largest_number(["-5", 5, "0"])


if __name__ == "__main__":
    unittest.main()
