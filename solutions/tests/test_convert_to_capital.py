# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 03 01 2025

@author: Kareiman Altayeb
"""

import unittest

# To test convert_to_capital
from solutions.convert_to_capital import convert_to_capital


class TestConvertCapitalLetters(unittest.TestCase):
    "Tests convert_to_capital function"

    # Standard test cases

    def test_all_small_letters(self):
        """It should convert all letters to capital"""
        self.assertEqual(convert_to_capital("kareiman"), "KAREIMAN")

    def test_some_are_capital_letters(self):
        """It should convert all letters to capital"""
        self.assertEqual(convert_to_capital("kAREiMan"), "KAREIMAN")

    def test_full_sentence(self):
        """It should convert all words to capital"""
        self.assertEqual(convert_to_capital("happy new year"), "HAPPY NEW YEAR")

    # Edge cases

    def test_mixed_with_numbers(self):
        """It should return the numbers the same"""
        self.assertEqual(convert_to_capital("12345kareiman"), "12345KAREIMAN")

    def test_special_characters(self):
        """It should return special characters the same"""
        self.assertEqual(convert_to_capital("?!!!"), "?!!!")

    # Defensive tests

    def test_empty_entry(self):
        """It should raise an error for space or empty entry"""
        with self.assertRaises(AssertionError):
            convert_to_capital("")


if __name__ == "__main__":
    unittest.main()
