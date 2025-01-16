"""
Unit tests for the `anagram_finder` function.

These tests validate the correct behavior of the function,
covering edge cases, defensive assertions, and typical usage scenarios.

Created on 14 01 2025
@author: Frankline Ambetsa
"""

import unittest
from solutions.anagram_finder import anagram_finder


class TestAnagramFinder(unittest.TestCase):
    """Unit tests for the anagram_finder function."""

    def test_valid_anagrams(self):
        """Test valid anagrams."""
        self.assertTrue(anagram_finder("listen", "silent"))
        self.assertTrue(anagram_finder("evil", "vile"))
        self.assertTrue(anagram_finder("a gentleman", "elegant man"))

    def test_invalid_anagrams(self):
        """Test invalid anagrams."""
        self.assertFalse(anagram_finder("hello", "world"))
        self.assertFalse(anagram_finder("python", "java"))
        self.assertFalse(anagram_finder("abc", "abcd"))  # Strings of different lengths

    def test_case_insensitivity(self):
        """Test case-insensitivity."""
        self.assertTrue(anagram_finder("Listen", "Silent"))
        self.assertTrue(anagram_finder("Evil", "Vile"))
        self.assertTrue(anagram_finder("Anagram", "Nagaram"))  # Case insensitive

    def test_empty_strings(self):
        """Test behavior with empty strings."""
        self.assertTrue(anagram_finder("", ""))  # Both empty
        with self.assertRaises(AssertionError):
            anagram_finder("", "non-empty")
        with self.assertRaises(AssertionError):
            anagram_finder("non-empty", "")

    def test_special_characters(self):
        """Test handling of special characters."""
        self.assertTrue(anagram_finder("Clint Eastwood", "Old West Action"))
        self.assertFalse(anagram_finder("hello world", "world! hello"))
        self.assertTrue(anagram_finder("!@#$%", "%$#@!"))  # Special characters only

    def test_different_lengths(self):
        """Test behavior with strings of different lengths."""
        self.assertFalse(anagram_finder("abc", "abcd"))
        self.assertFalse(anagram_finder("short", "longer"))
        self.assertFalse(
            anagram_finder("a", "longerstring")
        )  # One character vs a longer string

    def test_invalid_inputs(self):
        """Test behavior with invalid inputs."""
        with self.assertRaises(AssertionError):
            anagram_finder(None, "valid")
        with self.assertRaises(AssertionError):
            anagram_finder("valid", None)
        with self.assertRaises(AssertionError):
            anagram_finder(123, "valid")
        with self.assertRaises(AssertionError):
            anagram_finder("valid", 456)


if __name__ == "__main__":
    unittest.main()
