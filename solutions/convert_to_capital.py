# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This function asks user to enter a word and converts the letters
to capital. The function will return numbers and capital letters the same

Created on 31 12 2024

@author: Kareiman Altayeb
"""


def convert_to_capital(user_text: str) -> str:
    """Asks the user to enter a text and returns the text in capital

    parameters:
        user_text = in str
    returns:
        user_text in capital letters

    raises:
        AssertionError: if input is empty

    examples:
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
