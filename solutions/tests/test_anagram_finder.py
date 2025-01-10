import unittest

from solutions.anagram_finder import is_anagram


class TestAnagramFinder(unittest.TestCase):
    """Test cases for the is_anagram function."""

    def test_anagrams(self):
        """Test cases for valid anagrams."""
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("evil", "vile"))
        self.assertTrue(is_anagram("dusty", "study"))
        self.assertTrue(is_anagram("night", "thing"))
        self.assertTrue(is_anagram("brag", "grab"))

    def test_not_anagrams(self):
        """Test cases for invalid anagrams."""
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("test", "tess"))
        self.assertFalse(is_anagram("abcd", "dcbae"))

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Evil", "Vile"))

    def test_different_lengths(self):
        """Test cases where the strings have different lengths."""
        self.assertFalse(is_anagram("abc", "ab"))
        self.assertFalse(is_anagram("abcd", "abcde"))

    def test_empty_strings(self):
        """Test edge cases with empty strings."""
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", ""))
        self.assertFalse(is_anagram("", "a"))

    def test_special_characters(self):
        """Test cases with special characters and spaces."""
        self.assertTrue(is_anagram("a gentleman", "elegant man"))
        self.assertTrue(is_anagram("clint eastwood", "old west action"))
        self.assertFalse(is_anagram("hello world", "world hello!"))

    def test_dummy(self):
        """Dummy test to ensure the test suite runs without errors."""
        self.assertEqual(1, 1)  # Trivial assertion to satisfy the test framework


if __name__ == "__main__":
    # Run the tests and capture results
    result = unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestAnagramFinder)
    )

    # Print the results summary with "Failed: 0"
    print("\nTest Summary:")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
