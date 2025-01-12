"""
A module that converts strings to either integer of float
Module content:
-convert_str_to_number(): takes a strings and returns a float of integer

Created on 8/01/2025
@author: Arwa Mohamed

"""


def convert_str_to_number(input_str: str) -> int | float:
    """Converts a string to a number (integer or float).

    Parameters:
        input_str (str): The string to convert to a number.
        - Must be a non-empty string.
        - Must not contain leading or trailing spaces.

    Returns:
        int: If the string represents an integer.
        float: If the string represents a float.

    Raises:
        ValueError: If the input is not valid number or it is not a string.

    Examples:
        >>> convert_str_to_number("42")
        42

        >>> convert_str_to_number("3.14")
        3.14

        >>> convert_str_to_number("1.4")
        1.4

    """
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string.")
    # returns an error in case the input is not a string
    try:
        if "." in input_str:
            return float(input_str)
        return int(input_str)
    except ValueError as exc:
        raise ValueError(f"Cannot convert '{input_str}' to a number.") from exc
