"""
Test module for Remove Duplicate function.

Created on 2024-01-10
Author: Safaa Osman

"""

import unittest

from ..Remove_Duplicates import Remove_Duplicates


class TestRemoveDuplicates(unittest.TestCase):
    """Test the Remove_Duplicates function - some tests are buggy!"""

    def test_empty_list(self):
        """It should return [] for an empty list"""
        self.assertEqual(Remove_Duplicates([]), [])

    def test_no_duplicates(self):
        """It should return the same list for list without duplicates"""
        self.assertEqual(Remove_Duplicates([1, 2, 3]), [1, 2, 3])

    def test_not_list(self):
        """It should raise AssertionError for non-list input"""
        with self.assertRaises(AssertionError):
            Remove_Duplicates("123")

    def test_All_duplicates(self):
        """It should return the list of one item that duplicates"""
        self.assertEqual(Remove_Duplicates([1, 1, 1, 1, 1, 1]), [1])

    def test_list_with_duplicates(self):
        """It should return the list without duplicates"""
        self.assertEqual(Remove_Duplicates([1, 1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_Mix_types_of_elements(self):
        """It should return the list of elements without duplicates"""
        self.assertEqual(
            Remove_Duplicates([1, "Safaa", 3.5, "Safaa", "safaa", 3.5]),
            [1, "Safaa", 3.5, "safaa"],
        )
