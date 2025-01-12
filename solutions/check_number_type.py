"""
This function asks the user to enter a number and checks if the number
is even or odd. It then returns the result as a string.

Created on 05 01 2025
@author: Eman Alfalouji.

"""


def check_number_type(user_input: str) -> str:
    """
    The function asks the user to enter a number and determines if it is type (even or odd.)


    Parameters:
        user_input (str): str
        A string that represents an integer.
        Floats or non-integer formats are not allowed.
    Raises:
        ValueError: If the input is empty.
        ValueError: If the input is not a valid integer.

    Returns:
        results will be a text whether "The number is even", "The number is odd"
        or raises an appropriate error.
        Examples :
        >>> check_number_type("20")
        "The number is even"
        >>> check_number_type("11")
        "The number is odd"
        >>> check_number_type("-11")
        "The number is odd"
        >>> check_number_type("")
        Traceback (most recent call last):
        ...
        ValueError:"Input cannot be empty. Enter a valid number."
        >>> check_number_type("Eman")
        Traceback (most recent call last):
        ...
        ValueError:"Please enter a valid number"




    """
    user_input = user_input.strip()
    # Check if it is empty
    if not user_input:
        raise ValueError("Input cannot be empty. Enter a valid number.")
    # check if it is a number
    if not user_input.lstrip("-").isdigit():
        raise ValueError("Please enter a valid number")
    number = int(user_input)
    # Check if the number is even or odd
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
