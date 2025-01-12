#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting hours to minutes.

Module contents:
    - convert_hours_to_minutes: calculates the time in minutes based on hours.

Created on 31-12-2024
@author: Azza Omer
"""


def convert_hours_to_minutes(hour_wasted: int) -> int:
    """
    Convert hours to minutes.

    Parameters:
        hour_wasted (int): The number of hours wasted. Must be a positive integer.

    Returns:
        int: The equivalent time in minutes.

    Examples:
        >>> convert_hours_to_minutes(1)
        60
        >>> convert_hours_to_minutes(5)
        300
        >>> convert_hours_to_minutes(12)
        720
        >>> convert_hours_to_minutes(0)
        0
        >>> convert_hours_to_minutes(3)
        180
        >>> convert_hours_to_minutes("2")  # Raises AssertionError
        Traceback (most recent call last):
            ...
        AssertionError: hour_wasted must be an integer.
        >>> convert_hours_to_minutes(-5)   # Raises AssertionError
        Traceback (most recent call last):
            ...
        AssertionError: hour_wasted must be greater than or equal to 0.
    """
    assert isinstance(hour_wasted, int), "hour_wasted must be an integer."
    assert hour_wasted >= 0, "hour_wasted must be greater than or equal to 0."
    minutes = hour_wasted * 60
    return minutes
