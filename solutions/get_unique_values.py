"""
This module provides functionality to extract unique values from a CSV file.

It contains the `get_unique_values` function, which takes a file path and
column name as input and returns a list of unique values from that column.
The module handles potential errors like invalid file paths or missing column
names.
"""

import csv


def get_unique_values(file_path: str, column_name: str) -> list:
    """
    Get unique values from a specified column in a CSV file.

    Parameters:
        file_path (str): Path to the CSV file. It should be a valid path to an existing CSV file.
                         The function assumes the file is encoded in UTF-8. Both relative and absolute
                         paths are acceptable. The file must exist, or a FileNotFoundError will be raised.
        column_name (str): Name of the column to extract unique values. It should correspond to a
                           header in the CSV file.
    Returns:
        list: Unique values in the specified column. The order of the unique values is not guaranteed to be
              the same as their order of appearance in the CSV file.

    Raises:
        FileNotFoundError: If the file path is invalid or the file does not exist.
        KeyError: If the column name doesn't exist in the CSV.
        ValueError: If the `file_path` is an empty string.

    Examples:
        >>> with open("test.csv", "w", newline="") as f:
        ...     writer = csv.writer(f)
        ...     writer.writerow(["Name", "Age", "City"])
        ...     writer.writerow(["Alice", "25", "New York"])
        ...     writer.writerow(["Bob", "30", "London"])
        ...     writer.writerow(["Alice", "25", "Paris"])
        >>> get_unique_values("test.csv", "Name")
        ['Bob', 'Alice']
        >>> get_unique_values("test.csv", "City")
        ['Paris', 'New York', 'London']
        >>> get_unique_values("test.csv", "Age")
        ['30', '25']
        >>> get_unique_values("test.csv", "Country")
        Traceback (most recent call last):
        ...
        KeyError: "Column 'Country' does not exist in the CSV."
        >>> get_unique_values("nonexistent_file.csv", "Name")
        Traceback (most recent call last):
        ...
        FileNotFoundError: File not found: nonexistent_file.csv
        >>> get_unique_values("", "Name")
        Traceback (most recent call last):
        ...
        ValueError: The file_path cannot be an empty string.
    """
    if not file_path:
        raise ValueError("The file_path cannot be an empty string.")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Check if the column name exists in the CSV header
            if column_name not in reader.fieldnames:
                raise KeyError(f"Column '{column_name}' does not exist in the CSV.")

            unique_values = set()
            # Iterate through the rows and add unique values to the set
            for row in reader:
                unique_values.add(row[column_name])

        return list(unique_values)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
