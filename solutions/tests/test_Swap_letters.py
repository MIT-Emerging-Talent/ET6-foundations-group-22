"""
Created on 08/01/2024

@author: Tibyan Khalid
"""

import unittest

from ..Swap_letters import Swap_letters


class TestSwapletters(unittest.TestCase):
    """Unittests for the Swap_letters function"""

    def test_lowercase_all(self):
        "Testing from lowercase to uppercase"
        self.assertEqual(Swap_letters("tibyan"), "TIBYAN")

    def test_uppercase_all(self):
        "Testing from uppercase to lowercase"
        self.assertEqual(Swap_letters("TIBYAN"), "tibyan")

    def test_mixed_cases(self):
        "Testing mixed spaces"
        self.assertEqual(Swap_letters("TiByAn"), "tIbYaN")

    def test_non_string_entry(self):
        "Raise an error if entry is not a string"
        with self.assertRaises(AssertionError):
            Swap_letters(57)

    def test_spaces(self):
        "Handle spaces correctly"
        self.assertEqual(Swap_letters("Hello World"), "hELLO wORLD")


if __name__ == "__main__":
    unittest.main()
