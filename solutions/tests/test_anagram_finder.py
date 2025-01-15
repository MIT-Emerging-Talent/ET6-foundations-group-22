"""
Unit tests for the `anagram_finder` function.

These tests ensure correct behavior of the `anagram_finder` function,
including standard merging, conflict resolution, edge cases, and input validation.

Created on 13 01 2025
@author: Frankline Ambetsa
"""

import unittest
from solutions.anagram_finder import anagram_finder


class TestAnagramFinder(unittest.TestCase):
    """Test cases for the anagram_finder function."""

    def test_anagrams(self):
        """Test cases for valid anagrams."""
        self.assertTrue(anagram_finder("listen", "silent"))
        self.assertTrue(anagram_finder("evil", "vile"))
        self.assertTrue(anagram_finder("dusty", "study"))
        self.assertTrue(anagram_finder("night", "thing"))
        self.assertTrue(anagram_finder("brag", "grab"))

    def test_not_anagrams(self):
        """Test cases for invalid anagrams."""
        self.assertFalse(anagram_finder("hello", "world"))
        self.assertFalse(anagram_finder("python", "java"))
        self.assertFalse(anagram_finder("test", "tess"))
        self.assertFalse(anagram_finder("abcd", "dcbae"))

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertTrue(anagram_finder("Listen", "Silent"))
        self.assertTrue(anagram_finder("Evil", "Vile"))

    def test_different_lengths(self):
        """Test cases where the strings have different lengths."""
        self.assertFalse(anagram_finder("abc", "ab"))
        self.assertFalse(anagram_finder("abcd", "abcde"))

    def test_empty_strings(self):
        """Test edge cases with empty strings."""
        self.assertTrue(
            anagram_finder("", "")
        )  # Both empty strings should be considered anagrams
        with self.assertRaises(AssertionError):
            anagram_finder(
                "a", ""
            )  # A non-empty string and empty string shouldn't be anagrams
        with self.assertRaises(AssertionError):
            anagram_finder(
                "", "b"
            )  # An empty string and non-empty string shouldn't be anagrams

    def test_special_characters(self):
        """Test cases with special characters and spaces."""
        self.assertTrue(anagram_finder("a gentleman", "elegant man"))
        self.assertTrue(anagram_finder("clint eastwood", "old west action"))
        self.assertFalse(anagram_finder("hello world", "world hello!"))

    def test_defensive_assertions(self):
        """Test defensive assertions for invalid inputs."""
        with self.assertRaises(AssertionError):
            anagram_finder(123, "silent")  # Non-string input
        with self.assertRaises(AssertionError):
            anagram_finder("listen", 123)  # Non-string input

        with self.assertRaises(AssertionError):
            anagram_finder("a", "")  # Empty string as second argument
        with self.assertRaises(AssertionError):
            anagram_finder("", "b")  # Empty string as first argument


if __name__ == "__main__":
    # Run the tests
    unittest.main()
