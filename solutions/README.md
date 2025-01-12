# Solutions

This folder contains implementations for the challenges.

## Challenges

1. **Merge Dictionaries**:
   - A utility to merge two dictionaries with conflict resolution.
   - See `merge_dictionaries.py` for the implementation.

2. **Anagram Finder**:
   - A function to check if two strings are anagrams.
   - See `anagram_finder.py` for the implementation.

## Usage

To use any solution, simply import the
required function and pass the appropriate arguments.

### How to Run

1. Clone the repository.
2. Navigate to the folder containing the solution.
3. Run the desired script:

    ```bash
    python <script_name>.py
    ```

### Example

```python
# Example for Anagram Finder
from anagram_finder import are_anagrams

result = are_anagrams("listen", "silent")
print(result)  # Output: True
