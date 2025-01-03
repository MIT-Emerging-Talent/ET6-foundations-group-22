import unittest
from get_unique_values import get_unique_values


class TestGetUniqueValues(unittest.TestCase):
    def test_unique_values(self):
        self.assertEqual(get_unique_values([1, 2, 2, 3]), {1, 2, 3})

    def test_empty_list(self):
        self.assertEqual(get_unique_values([]), set())

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_unique_values("not a list")


if __name__ == "__main__":
    unittest.main()
