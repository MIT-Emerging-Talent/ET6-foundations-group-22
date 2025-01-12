"""
This function asks the user to enter numbers and return the sum of the numbers  .

Created on 05 01 2025
@author: Eman Alfalouji.

"""

from typing import List, Union


def sum_of_list(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list): A list of numbers (int or float).

    Returns:
        int/float: The sum of the numbers in the list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an int or float.

    Examples :
        >>> sum_of_list([1,2,5])
        The sum of the list is:8
        >>> sum_of_list([-1,-2,-5])
        The sum of the list is:-8
        >>> sum_of_list([-1,-2,"l"])
        Please enter valid numbers separated by spaces.
        >>> sum_of_list(["l"])
        Please enter valid numbers separated by spaces.
        >>> sum_of_list([])
        Please enter valid numbers separated by spaces.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be int or float.")
    return sum(numbers)
