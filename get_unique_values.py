def get_unique_values(lst):
    """
    Returns a set of unique values from a given list.

    Args:
        lst (list): The list from which to extract unique values.

    Returns:
        set: A set containing the unique values in the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return set(lst)
