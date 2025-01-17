""" "
Created on 0084/01/2025
@author: Arwa Mohamed

"""

import unittest


def kg_to_lbs(kg):
    """
    Converts a given weight from kilograms (kg) to pounds (lbs).

    Args:
        kg (float): Weight in kilograms.

    Returns:
        float: Equivalent weight in pounds.

    Raises:
        ValueError: If the input is not a positive number.
    """
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462


class TestKgToLbs(unittest.TestCase):
    def test_positive_conversion(self):
        self.assertAlmostEqual(kg_to_lbs(1), 2.20462, places=5)
        self.assertAlmostEqual(kg_to_lbs(5), 11.0231, places=4)

    def test_zero_conversion(self):
        self.assertEqual(kg_to_lbs(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            kg_to_lbs(-1)

    def test_large_value(self):
        self.assertAlmostEqual(kg_to_lbs(1000), 2204.62, places=2)


if __name__ == "__main__":
    unittest.main()
