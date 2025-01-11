# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module that converts letters to uppercase

Created on 31 12 2024

@author: Kareiman Altayeb
"""


def convert_to_capital(user_text: str) -> str:
    """Asks the user to enter a text and returns the text in capital

    Parameters:
        user_text (str): The user input text to be converted to uppercase.

    Returns:
        (str) : user_text in capital letters

    Raises:
        AssertionError: If the input is empty or contains only spaces.

    Examples:
    >>> convert_to_capital('hello')
        'HELLO'
    >>> convert_to_capital('HelLo')
        'HELLO'
    >>> convert_to_capital('123hello')
        '123HELLO'
    """

    user_text = user_text.strip()

    if not user_text:
        raise AssertionError("Entry cannot be empty or just spaces")

    return user_text.upper()
