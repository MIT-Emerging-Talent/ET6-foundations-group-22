"""
Created on 04/01/2025

@author: Tibyan Khalid
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Unittests for the is_palindrome function"""

    def test_palindrome(self):
        self.assertEqual(is_palindrome("level"), "Palindrome")

    def test_not_palindrome(self):
        self.assertEqual(is_palindrome("world"), "Not Palindrome")

    # Boundary Cases Tests
    def test_empty_string(self):
        "Empty string is considered a Palindrome"
        self.assertEqual(is_palindrome(""), "Palindrome")

    def test_single_character(self):
        "Any single character is a palindrome as it reads the same backward"
        self.assertEqual(is_palindrome("t"), "Palindrome")

    def test_non_string_entry(self):
        "Raise an error if entry is not a string"
        with self.assertRaises(AssertionError):
            is_palindrome(34)

    def test_upper_lower_cases(self):
        "Case matters here, radar is a Palindrome but Radar is not"
        self.assertEqual(is_palindrome("Radar"), "Not Palindrome")
        self.assertEqual(is_palindrome("Radar".lower()), "Palindrome")

    def test_special_characters(self):
        "Handles special characters correctly"
        self.assertEqual(is_palindrome("t@a@t"), "Palindrome")
        self.assertEqual(is_palindrome("a@b@c"), "Not Palindrome")
