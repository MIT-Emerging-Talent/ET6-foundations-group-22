# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the area of a square given the side_length

Module contents:
    calculate_square_area: calculates the area of a square

Created on 04 01 2025
@author: Kareiman Altayeb
"""


def calculate_square_area(side_length: float) -> float:
    """The function asks the user to enter the side length of the square
    and the function returns the area of the square.

    parameter:
    side_length in integer or float

    raises:
    AssertionError: if side_length was =< 0
    ValueError: if the value entered was or str or text

    returns:
    side_length ** 2

    >>> calculate_square_area(5)
    25

    >>> calculate_square_area(12.30)
    151.91

    >>> calculate_square_area(0.42)
    0.1764

    """
    # The entry cannot be a text or letters, only numbers
    assert isinstance(side_length, (int, float)), "input must be a number"

    if side_length <= 0:
        raise AssertionError("side length must be bigger than zero")

    return side_length**2
