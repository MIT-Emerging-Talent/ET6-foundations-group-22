# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module that converts all letters to uppercase

Created on 31 12 2024

@author: Kareiman Altayeb
"""


def convert_to_uppercase(user_text: str) -> str:
    """Asks the user to enter a text and returns the text in capital
    with all characters in uppercase

    Parameters:
        user_text (str): The user input text to be converted to uppercase.

    Returns:
        str : user_text in upper case

    Raises:
        AssertionError: If the input is empty or contains only spaces.

    Examples:
    >>> convert_to_uppercase('hello')
        'HELLO'
    >>> convert_to_uppercase('HelLo')
        'HELLO'
    >>> convert_to_uppercase('123hello')
        '123HELLO'
    """

    user_text = user_text.strip()

    if not user_text:
        raise AssertionError("Entry cannot be empty or just spaces")

    return user_text.upper()
