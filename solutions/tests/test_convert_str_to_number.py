""" "
Created on 0084/01/2025
@author: Arwa Mohamed

"""

import unittest


def convert_to_number(input_str):
    """Converts a string to a number (integer or float).

    Parameters:
        input_str (str): The string to convert to a number.

    Returns:
        int: If the string represents an integer.
        float: If the string represents a float.

    Examples:
        >>> convert_to_number("42")
        42

        >>> convert_to_number("3.14")
        3.14

    Raises:
        ValueError: If the input string cannot be converted to a number.
    """
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string.")

    try:
        if "." in input_str:
            return float(input_str)
        return int(input_str)
    except ValueError:
        raise ValueError(f"Cannot convert '{input_str}' to a number.")


class TestConvertToNumber(unittest.TestCase):
    """Unit tests for the convert_to_number function.

    The tests verify:
    - Conversion of valid integer strings to integers.
    - Conversion of valid float strings to floats.
    - Handling of invalid strings (non-numeric).
    - Error handling for non-string inputs.
    """

    def test_valid_integer_string(self):
        """Test conversion of valid integer strings."""
        self.assertEqual(convert_to_number("42"), 42)
        self.assertEqual(convert_to_number("-7"), -7)

    def test_valid_float_string(self):
        """Test conversion of valid float strings."""
        self.assertEqual(convert_to_number("3.14"), 3.14)
        self.assertEqual(convert_to_number("-0.001"), -0.001)

    def test_invalid_string(self):
        """Test behavior with invalid strings."""
        with self.assertRaises(ValueError):
            convert_to_number("abc")
        with self.assertRaises(ValueError):
            convert_to_number("123abc")

    def test_non_string_input(self):
        """Test error handling for non-string inputs."""
        with self.assertRaises(ValueError):
            convert_to_number(123)
        with self.assertRaises(ValueError):
            convert_to_number(None)
        with self.assertRaises(ValueError):
            convert_to_number([1, 2, 3])


if __name__ == "_main_":
    unittest.main()
