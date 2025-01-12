"""
This module contains the implementation of the `merge_dictionaries` function.

The `merge_dictionaries` function allows merging two dictionaries into one,
with support for resolving key conflicts through a custom resolution function.

Created on 03 01 2025
@author: Frankline Ambetsa
"""


def merge_dictionaries(dict1, dict2, conflict_resolution=None):
    """
    Merge two dictionaries into one.

    If keys conflict, a conflict resolution function can be provided
    to decide which value to keep. If no function is provided, the value
    from `dict2` will overwrite the value from `dict1`.

    Parameters:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
        conflict_resolution (function, optional): A function that takes
            two arguments (value1, value2) and returns the resolved value.

    Returns:
        dict: A merged dictionary.

    Raises:
        AssertionError: If `dict1` or `dict2` is not a dictionary.
        AssertionError: If `conflict_resolution` is not callable when provided.

    Examples:
        >>> merge_dictionaries({'a': 1}, {'a': 2, 'b': 3})
        {'a': 2, 'b': 3}
        >>> merge_dictionaries({'a': 1}, {'a': 2, 'b': 3}, max)
        {'a': 2, 'b': 3}
        >>> merge_dictionaries({'x': 1}, {'y': 2})
        {'x': 1, 'y': 2}
    """
    # Defensive assertions
    assert isinstance(dict1, dict), "dict1 must be a dictionary."
    assert isinstance(dict2, dict), "dict2 must be a dictionary."
    if conflict_resolution is not None:
        assert callable(conflict_resolution), (
            "conflict_resolution must be a callable function."
        )

    merged = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged and conflict_resolution:
            # Resolve conflict using the provided function
            merged[key] = conflict_resolution(merged[key], value)
        else:
            # Add or overwrite key with dict2's value
            merged[key] = value

    return merged
