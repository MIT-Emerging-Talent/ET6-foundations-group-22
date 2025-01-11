"""
Anagram Finder Module

This module provides a function to determine if two strings are anagrams of each other.
It checks if the strings are anagrams, handling edge cases like empty strings, special characters, and case-insensitivity.

Created on 03 01 2025
@author: Frankline Ambetsa
"""

import doctest


def is_anagram(string1: str, string2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Anagrams are words or phrases made by rearranging the letters of another word or phrase.
    This function will check for anagram status while ignoring spaces and case sensitivity.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        ValueError: If any string is empty except when both are empty.

    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("evil", "vile")
    True
    >>> is_anagram("hello", "world")
    False
    >>> is_anagram("a gentleman", "elegant man")
    True
    >>> is_anagram("clint eastwood", "old west action")
    True
    """

    # Defensive assertions for valid string inputs
    assert isinstance(string1, str), "string1 must be a string"
    assert isinstance(string2, str), "string2 must be a string"

    # If any string is empty, raise an error, unless both are empty
    if string1 == "" and string2 == "":
        return True  # Both empty strings are considered anagrams of each other

    if string1 == "":
        raise AssertionError("string1 cannot be empty")
    if string2 == "":
        raise AssertionError("string2 cannot be empty")

    # Remove spaces and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if sorted strings are equal (anagram check)
    return sorted(string1) == sorted(string2)


# Run doctests when executed directly
if __name__ == "__main__":
    doctest.testmod()
