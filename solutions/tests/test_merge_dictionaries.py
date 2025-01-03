# solutions/tests/test_merge_dictionaries.py

import unittest
from solutions.merge_dictionaries import merge_dictionaries


class TestMergeDictionaries(unittest.TestCase):
    def test_no_conflicts(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_overwrite_conflicts(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_conflict_resolution_max(self):
        dict1 = {"a": 1, "b": 5}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 5, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2, max), expected)

    def test_conflict_resolution_min(self):
        dict1 = {"a": 1, "b": 5}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2, min), expected)

    def test_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_one_empty_dict(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {}
        expected = {"a": 1, "b": 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_only_conflicts(self):
        dict1 = {"a": 1}
        dict2 = {"a": 2}
        expected = {"a": 2}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)


if __name__ == "__main__":
    unittest.main()
