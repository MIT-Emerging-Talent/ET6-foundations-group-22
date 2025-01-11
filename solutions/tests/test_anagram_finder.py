"""
Unit tests for the `is_anagram` function.

These tests ensure correct behavior of the `is_anagram` function,
including standard anagram checking, edge cases, input validation, and defensive assertions.

Created on 03 01 2025
@author: Frankline Ambetsa
"""

import unittest
from solutions.anagram_finder import is_anagram


class TestAnagramFinder(unittest.TestCase):
    """Test cases for the is_anagram function."""

    def test_anagrams(self):
        """Test cases for valid anagrams."""
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("evil", "vile"))
        self.assertTrue(is_anagram("dusty", "study"))
        self.assertTrue(is_anagram("night", "thing"))
        self.assertTrue(is_anagram("brag", "grab"))

    def test_not_anagrams(self):
        """Test cases for invalid anagrams."""
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("test", "tess"))
        self.assertFalse(is_anagram("abcd", "dcbae"))

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Evil", "Vile"))

    def test_different_lengths(self):
        """Test cases where the strings have different lengths."""
        self.assertFalse(is_anagram("abc", "ab"))
        self.assertFalse(is_anagram("abcd", "abcde"))

    def test_empty_strings(self):
        """Test edge cases with empty strings."""
        self.assertTrue(
            is_anagram("", "")
        )  # Both empty strings should be considered anagrams
        with self.assertRaises(AssertionError):
            is_anagram(
                "a", ""
            )  # A non-empty string and empty string shouldn't be anagrams
        with self.assertRaises(AssertionError):
            is_anagram(
                "", "b"
            )  # An empty string and non-empty string shouldn't be anagrams

    def test_special_characters(self):
        """Test cases with special characters and spaces."""
        self.assertTrue(is_anagram("a gentleman", "elegant man"))
        self.assertTrue(is_anagram("clint eastwood", "old west action"))
        self.assertFalse(is_anagram("hello world", "world hello!"))

    def test_defensive_assertions(self):
        """Test defensive assertions for invalid inputs."""
        with self.assertRaises(AssertionError):
            is_anagram(123, "silent")  # Non-string input
        with self.assertRaises(AssertionError):
            is_anagram("listen", 123)  # Non-string input

        with self.assertRaises(AssertionError):
            is_anagram("a", "")  # Empty string as second argument
        with self.assertRaises(AssertionError):
            is_anagram("", "b")  # Empty string as first argument


if __name__ == "__main__":
    # Run the tests
    unittest.main()
