"""
Test module for Time Conversion function.
Contains intentionally buggy tests for debugging practice.

Created on 2024-01-09
Author: Safaa Osman
"""

import unittest
from ..Time_Conversion import Time_Conversion


class TestTimeConversion(unittest.TestCase):
    """Test suite for the Time Conversion function"""

    def test_equal_minutes_hours(self):
        """It should return the time conversion properly"""
        self.assertEqual(Time_Conversion("12:12"), "20:12")

    def test_regular_time(self):
        """It should return the time conversion properly"""
        self.assertEqual(Time_Conversion("08:00"), "16:00")

    # Boundary cases

    def test_minimum_time(self):
        """It should return the time conversion properly"""
        self.assertEqual(Time_Conversion("00:00"), "08:00")

    def test_maximum_time(self):
        """It should return the time conversion properly"""
        self.assertEqual(Time_Conversion("23:59"), "07:59")

    # Defensive cases

    def test_not_string(self):
        """It should raise AssertionError for input not string"""
        with self.assertRaises(AssertionError):
            Time_Conversion(1230)

    def test_hours_out_of_range(self):
        """It should raise ValueError for hours are out of range"""
        with self.assertRaises(ValueError):
            Time_Conversion("25:30")

    def test_minutes_out_of_range(self):
        """It should raise ValueError for minutes are out of range"""
        with self.assertRaises(ValueError):
            Time_Conversion("12:69")

    def test_empty_string(self):
        """It should raise AssertionError for string is empty"""
        with self.assertRaises(AssertionError):
            Time_Conversion("")

    def test_mix_types(self):
        """It should raise AssertionError for string is mix types"""
        with self.assertRaises(AssertionError):
            Time_Conversion("hg:45")

    def test_invalid_minutes(self):
        """It should raise ValueError for minutes are out of range"""
        with self.assertRaises(ValueError):
            Time_Conversion("00:60")

    def test_invalid_hours(self):
        """It should raise ValueError for minutes are out of range"""
        with self.assertRaises(ValueError):
            Time_Conversion("24:00")
