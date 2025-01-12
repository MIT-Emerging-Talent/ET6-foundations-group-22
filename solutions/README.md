# Solutions

## Merge Dictionaries Solution

This repository contains a Python solution to merge two dictionaries.
The solution merges two dictionaries by resolving conflicts based on an optional
 conflict resolution function.

### Features

- Merges two dictionaries.
- Resolves conflicts with a custom function, or by default, `dict2` overwrites `dict1`.

### How to Run

1. Clone the repository.
2. Install dependencies (if any).
3. Run the tests:

    ```bash
    python -m unittest solutions/tests/test_merge_dictionaries.py
    ```

### Example

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = merge_dictionaries(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
