"""
Created on 08/01/2024

@author: Tibyan Khalid

This file contains boundary cases and defensive assertion tests for the function Swap_letters.
"""

import unittest

from ..Swap_letters import Swap_letters


class TestSwapLettersFunctionality(unittest.TestCase):
    """Test cases for validating the behavior of the Swap_letters function,
    including edge cases and defensive assertions."""

    def test_lowercase_all(self):
        "Testing from lowercase to uppercase"
        self.assertEqual(Swap_letters("tibyan"), "TIBYAN")

    def test_uppercase_all(self):
        "Testing from uppercase to lowercase"
        self.assertEqual(Swap_letters("TIBYAN"), "tibyan")

    def test_mixed_cases(self):
        "Testing mixed spaces"
        self.assertEqual(Swap_letters("TiByAn"), "tIbYaN")

    def test_non_string_entry(self):
        "Raise an error if entry is not a string"
        with self.assertRaises(AssertionError):
            Swap_letters(57)

    def test_spaces(self):
        "Handle spaces correctly"
        self.assertEqual(Swap_letters("Hello World"), "hELLO wORLD")

    def test_empty_string(self):
        "Test for an empty string input"
        self.assertEqual(Swap_letters(""), "")

    def test_special_characters(self):
        "Test for special characters input"
        self.assertEqual(Swap_letters("1234!@#$"), "1234!@#$")


if __name__ == "__main__":
    unittest.main()
