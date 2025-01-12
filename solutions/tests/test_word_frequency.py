# test_word_frequency.py
"""
This module contains unit tests for the word_frequency module.

The tests verify the functionality of the count_word_frequency function,
which counts the frequency of words in a given text.
"""

import unittest

from ..word_frequency import count_word_frequency


class TestWordFrequency(unittest.TestCase):
    """Test cases for the count_word_frequency function."""

    def test_count_word_frequency(self):
        """Test counting word frequency in a simple text."""
        text = "hello world hello"
        expected_output = {"hello": 2, "world": 1}
        self.assertEqual(count_word_frequency(text), expected_output)

    def test_empty_text(self):
        """Test counting word frequency in an empty string."""
        text = ""
        expected_output = {}
        self.assertEqual(count_word_frequency(text), expected_output)

    def test_case_insensitive(self):
        """Test counting word frequency with case-insensitive matching."""
        text = "Hello hello HeLLo"
        expected_output = {"hello": 3}
        self.assertEqual(count_word_frequency(text), expected_output)


if __name__ == "__main__":
    unittest.main()
