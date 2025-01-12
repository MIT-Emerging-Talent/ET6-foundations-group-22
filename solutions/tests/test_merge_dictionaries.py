# solutions/tests/test_merge_dictionaries.py

"""
Unit tests for the `merge_dictionaries` function.

These tests ensure correct behavior of the `merge_dictionaries` function,
including standard merging, conflict resolution, edge cases, and input validation.

Created on 03 01 2025
@author: Frankline Ambetsa
"""

import unittest
from solutions.merge_dictionaries import merge_dictionaries


class TestMergeDictionaries(unittest.TestCase):
    """Unit tests for the `merge_dictionaries` function."""

    def test_no_conflicts(self):
        """It should merge dictionaries with no conflicting keys."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_overwrite_conflicts(self):
        """It should overwrite conflicting keys with values from dict2."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_conflict_resolution_max(self):
        """It should resolve conflicts using the max function."""
        dict1 = {"a": 1, "b": 5}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 5, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2, max), expected)

    def test_conflict_resolution_min(self):
        """It should resolve conflicts using the min function."""
        dict1 = {"a": 1, "b": 5}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2, min), expected)

    def test_empty_dicts(self):
        """It should return an empty dictionary when both inputs are empty."""
        dict1 = {}
        dict2 = {}
        expected = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_one_empty_dict(self):
        """It should return the non-empty dictionary when one input is empty."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {}
        expected = {"a": 1, "b": 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_only_conflicts(self):
        """It should overwrite keys with values from dict2 for conflicting keys."""
        dict1 = {"a": 1}
        dict2 = {"a": 2}
        expected = {"a": 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_non_dict_inputs(self):
        """It should raise a TypeError for non-dictionary inputs."""
        with self.assertRaises(AssertionError):
            merge_dictionaries([], {"a": 1})
        with self.assertRaises(AssertionError):
            merge_dictionaries({"a": 1}, 42)

    def test_invalid_conflict_resolution(self):
        """It should raise a ValueError for non-callable conflict resolution."""
        with self.assertRaises(AssertionError):
            merge_dictionaries({"a": 1}, {"a": 2}, conflict_resolution=42)


if __name__ == "__main__":
    unittest.main()
