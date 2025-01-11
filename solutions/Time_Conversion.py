"""
A module for Converting time from Eastern Standard Time zone (EST) to Arabia
Standard Time (AST)

Created on 2025-01-07
Author: Safaa Osman
"""


def Time_Conversion(est_time: str) -> str:
    """Returns a time in Arabia Standard Time zone (AST)

    Takes input time in the format HH:MM (24-hours format) and returns
    the equavelent time in AST in the same format.

    Parameters:
        EST_Time (str): time in EST in the format 24 hour

    Returns -> str: time in AST in the format 24 hour

    Raises:
        TypeError: if the input is not a string
        AssertionError: if the hours are not between the boundary of (0-23)
        AssertionError: if the minutes are not between the boundary of (0-59)
        AssertionError: if the input is empty string


    Examples:
    >>> Time_Conversion("14:30")
    '22:30'

    >>> Time_Conversion("8:15")
    '16:15'

    >>> Time_Conversion("0:0")
    '8:0'


    """
    assert est_time != "", "input should be a time in HH:MM format"

    assert isinstance(est_time, str), "The input must be string"

    # split the input to hours and minutes in integers
    hours, minutes = est_time.split(":")

    # Assert hours and minutes are numbers
    assert hours.isdigit(), "hours must be integers"
    assert minutes.isdigit(), "minutes must be integers"

    hours = int(hours)
    minutes = int(minutes)

    # Assert boundary
    if not (0 <= hours <= 23):
        raise ValueError("hours must be between 0 and 23")
    if not (0 <= minutes <= 59):
        raise ValueError("minutes must be between 0 and 59")

    hours += 8

    if hours >= 24:
        hours -= 24

    return f"{hours}:{minutes}"
