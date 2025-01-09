"""
Created on 08/01/2024

@author: Tibyan Khalid
"""


def Swap_letters(string: str) -> str:
    """Swap_letters will return the string given with switched cases.

    Parameters:
      String(str) "the word that will get modified"

    Returns: modified_string(str) "the string with swapped cases"

    >>> Swap_letters("hello")
    'HELLO'

    >>> Swap_letters("HELLO")
    'hello'

    >>> Swap_letters("HeLlO")
    'hElLo'
    """
    if not isinstance(string, str):
        "Make sure the expected input is a string"
        raise AssertionError("Input must be a string")

    changed_string = ""
    for char in string:
        if char.islower():
            changed_string = changed_string + char.upper()
        elif char.isupper():
            changed_string = changed_string + char.lower()
        else:
            changed_string = changed_string + char
    return changed_string
