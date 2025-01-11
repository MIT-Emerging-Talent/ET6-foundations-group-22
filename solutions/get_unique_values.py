# Module for extracting unique values from a CSV file.
"""
This module provides the get_unique_values function to extract
unique values from a specified column in a CSV file.
"""

import csv


def get_unique_values(file_path: str, column_name: str) -> list:
    """
    Get unique values from a specified column in a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.
        column_name (str): Name of the column to extract unique values.

    Returns:
        list: Unique values in the specified column.

    Raises:
        FileNotFoundError: If the file path is invalid.
        KeyError: If the column name doesn't exist in the CSV.

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
    """
    try:
        with open(file_path, "r") as file:
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
