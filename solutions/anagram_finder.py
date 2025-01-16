"""
Anagram Finder Module

This module provides a function to determine if two strings are anagrams of each other.
It checks if the strings are anagrams, handling edge cases like empty strings, special characters, and case-insensitivity.

Created on 13 01 2025
@author: Frankline Ambetsa
"""


def anagram_finder(string1: str, string2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        AssertionError: If the inputs are not valid strings or both are empty.

    Examples:
        >>> anagram_finder("listen", "silent")
        True
        >>> anagram_finder("a gentleman", "elegant man")
        True
        >>> anagram_finder("", "")
        True
        >>> anagram_finder("hello", "world")
        False
    """
    # Defensive assertions
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise AssertionError("Inputs must be valid strings")

    # Allow the case where both strings are empty
    if string1 == "" and string2 == "":
        return True

    # Ensure one string is not empty if the other is non-empty
    if string1.strip() == "" or string2.strip() == "":
        raise AssertionError("Both strings must be non-empty if not both empty")

    # Helper function: Normalize a string by removing spaces and converting to lowercase
    def normalize(s: str) -> str:
        return "".join(s.split()).lower()

    # Normalize both input strings
    normalized1 = normalize(string1)
    normalized2 = normalize(string2)

    # Compare the sorted versions of the normalized strings
    return sorted(normalized1) == sorted(normalized2)
