#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the largest number.

Module contents:
    - largest_number: Extracts the largest number from a list of integers.

Created on 11-01-2025
@author: Azza
"""


def largest_number(list_numbers: list) -> int:
    """Extract the largest number from the given list of integers.

    Args:
        list_numbers (list): A list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.

    Examples:
        >>> largest_number([0, 1, 9, 2, 6, 4])
        9
        >>> largest_number([12])
        12
        >>> largest_number([8, -1, -8, 5])
        8
        >>> largest_number([-9, -1, -6, -5])
        -1
        >>> largest_number([0, 0])
        0
        >>> largest_number([])  # Raises ValueError
        Traceback (most recent call last):
            ...
        ValueError: The list must not be empty.
        >>> largest_number(["-5", 5, "0"])  # Raises TypeError
        Traceback (most recent call last):
            ...
        TypeError: All elements in the list must be integers.
        >>> largest_number(42)  # Raises TypeError
        Traceback (most recent call last):
            ...
        TypeError: The input must be a list.
        >>> largest_number([2**32, 2**16, 2**8, 1])
        4294967296
    """

    # Ensure the input is a list of integers
    if not isinstance(list_numbers, list):
        raise TypeError("The input must be a list.")
    if not list_numbers:
        raise ValueError("The list must not be empty.")
    if not all(isinstance(i, int) for i in list_numbers):
        raise TypeError("All elements in the list must be integers.")

    return max(list_numbers)
