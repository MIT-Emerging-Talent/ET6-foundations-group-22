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
