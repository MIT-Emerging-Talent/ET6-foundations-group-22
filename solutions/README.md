# Solutions

This folder contains implementations for the challenges.

## Challenges

1. **Merge Dictionaries**:
   - A utility to merge two dictionaries with conflict resolution.
   - Resolves conflicts with a custom function, or by default, `dict2` overwrites `dict1`.
   - See `merge_dictionaries.py` for the implementation.

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
