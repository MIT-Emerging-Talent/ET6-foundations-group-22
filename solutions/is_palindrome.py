"""
Created on 04/01/2025

@author: Tibyan Khalid
"""


def is_palindrome(string):
    """is_palindrome fuction will return whether the entry given is a palindrome or not.
    Palindrome: a word whose reverse is the same as the original word.

     Parameters:
      string(str): the string to be checked.

     Returns:
      string (str): "Palindrome" if the word is a palindrome, otherwise "Not Palindrome".

     Raises:
      AssertionError: If the argument is not a string or if it's too long.

     >>> is_palindrome("RADAR")
     'Palindrome'

     >>> is_palindrome("radar")
     'Palindrome'

     >>> is_palindrome("Radar")
     'Not Palindrome'

     >>> is_palindrome("hello")
     'Not Palindrome'
    """
    # Defensive assertions
    assert isinstance(string, str), "Argument(Input) must be a string"
    assert len(string) <= 100, (
        "Argument (Input) is too long, max allowed length is 100 characters"
    )

    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
