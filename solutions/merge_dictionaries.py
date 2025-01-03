# solutions/merge_dictionaries.py


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

    Example:
        >>> merge_dictionaries({'a': 1}, {'a': 2, 'b': 3})
        {'a': 2, 'b': 3}
        >>> merge_dictionaries({'a': 1}, {'a': 2, 'b': 3}, max)
        {'a': 2, 'b': 3}
    """
    merged = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged and conflict_resolution:
            # Resolve conflict using the provided function
            merged[key] = conflict_resolution(merged[key], value)
        else:
            # Add or overwrite key with dict2's value
            merged[key] = value

    return merged


if __name__ == "__main__":
    # Example usage
    dict_a = {"x": 1, "y": 2}
    dict_b = {"y": 3, "z": 4}

    print("Default merge (dict_b overwrites):")
    print(merge_dictionaries(dict_a, dict_b))

    print("\nMerge with conflict resolution (max value):")
    print(merge_dictionaries(dict_a, dict_b, max))
