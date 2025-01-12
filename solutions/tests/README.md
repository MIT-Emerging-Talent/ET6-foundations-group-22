# Tests

## Tests for Dictionary Merging with Conflict Resolution

This folder contains unit tests for the dictionary merging and conflict resolution
 functionalities implemented in the `merge_dictionaries.py` script.

## Purpose

The purpose of the tests is to ensure that the dictionary merging logic,
including handling conflicts, works as expected. The tests verify that:

- Dictionaries are merged correctly.
- Conflict resolution logic (e.g., using the `max` function)
  is applied properly when keys conflict.
- Edge cases and various scenarios are handled appropriately.

## Test File Structure

- `test_merge_dictionaries.py`: Contains unit tests for the `merge_dictionaries`
  function. It includes tests for:
  - Default dictionary merging (where dictionary B overwrites dictionary A).
  - Conflict resolution merging (using the `max` value).
  - Various edge cases, such as empty dictionaries, overlapping keys, and more.

## Running the Tests

To run the tests, follow these steps:

1. **Navigate to the project root directory** (where the `solutions` folder is located):

   ```bash
   cd /path/to/your/project
   python -m unittest discover -s solutions/tests
