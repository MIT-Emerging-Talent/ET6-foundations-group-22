# Tests

This folder contains unit tests for the challenges in the `solutions` module.

## Purpose

The purpose of these tests is to ensure the functionality of the implemented solutions, including handling edge cases and verifying correct behavior.

## Test Files

- **`test_merge_dictionaries.py`**:
  - Tests for the Merge Dictionaries challenge.
  - Verifies:
    - Default dictionary merging (where dictionary B overwrites dictionary A).
    - Conflict resolution merging (e.g., using the `max` value).
    - Handling of edge cases, such as empty dictionaries and overlapping keys.

- **`test_anagram_finder.py`**:
  - Tests for the Anagram Finder challenge.
  - Ensures the function correctly identifies whether two strings are anagrams, handling both typical and edge cases.

## Running Tests

Run the following command to execute all tests:

```bash
python -m unittest discover -s solutions/tests -p "test_*.py"
