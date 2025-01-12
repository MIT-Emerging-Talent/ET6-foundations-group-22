"""
A module for removing duplicates from a list of numbers

Module contents:
  - Remove_Duplicates: Remove any duplicate numbers in the list

Created on 2025-1-4
@author: Safaa Osman
"""


def Remove_Duplicates(items: list) -> list:
    """
    This Function Removes any duplicates elements from the list

    Arguments: list of elements

    Returns: list of elements without duplicates.

    Raises:
    AssertionError: if the input is not a list


    Examples:
    >>> Remove_Duplicates(['a','b','a'])
    ['a', 'b']

    >>> Remove_Duplicates([1,1,2])
    [1, 2]

    >>> Remove_Duplicates([1,2,2,3,3,3])
    [1, 2, 3]

    >>> Remove_Duplicates([1])
    [1]

    >>> Remove_Duplicates([])
    []

    >>> Remove_Duplicates([5,5,5,5,5,5,5])
    [5]

    """
    assert isinstance(items, list), "input must be a list"

    Final_list = []
    for item in items:
        if item not in Final_list:
            Final_list.append(item)
    return Final_list
