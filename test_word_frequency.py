# test_word_frequency.py

import unittest
from word_frequency import count_word_frequency


class TestWordFrequency(unittest.TestCase):
    def test_count_word_frequency(self):
        text = "hello world hello"
        expected_output = {"hello": 2, "world": 1}
        self.assertEqual(count_word_frequency(text), expected_output)

    def test_empty_text(self):
        text = ""
        expected_output = {}
        self.assertEqual(count_word_frequency(text), expected_output)

    def test_case_insensitive(self):
        text = "Hello hello HeLLo"
        expected_output = {"hello": 3}
        self.assertEqual(count_word_frequency(text), expected_output)


if __name__ == "__main__":
    unittest.main()
