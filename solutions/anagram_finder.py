"""
Anagram Finder
This script provides a function to determine if two strings are anagrams.
"""


def is_anagram(string1: str, string2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Normalize strings: convert to lowercase and remove spaces
    string1 = "".join(string1.lower().split())
    string2 = "".join(string2.lower().split())

    # Compare sorted characters
    return sorted(string1) == sorted(string2)


if __name__ == "__main__":
    # Example usage
    word1 = "listen"
    word2 = "silent"
    print(f"Are '{word1}' and '{word2}' anagrams? {is_anagram(word1, word2)}")

    word3 = "hello"
    word4 = "world"
    print(f"Are '{word3}' and '{word4}' anagrams? {is_anagram(word3, word4)}")
