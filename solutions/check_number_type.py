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
        user_input (str):  str
    Raises:
        AssertionError: if the argument is not a integer or empty

    Returns:
        results will be a text whether "The number is even", "The number is odd"
        or "Enter a valid number "
        Examples :
        >>> check_number_type("20")
        "The number is even"
        >>> check_number_type("11")
        "The number is odd"
    """
    user_input = user_input.strip()
    # Check if it is empty
    if not user_input:
        raise ValueError("Input cannot be empty. Enter a valid number.")
    # check if it is a number
    if not user_input.lstrip("-").isdigit():
        raise ValueError("Enter a valid number")
    number = int(user_input)
    # Check if the number is even or odd
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
