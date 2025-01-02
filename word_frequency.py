# word_frequency.py


def count_word_frequency(text):
    """
    Function to count the frequency of each word in a given text.

    Args:
        text (str): Input text where word frequency needs to be counted.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    word_count = {}
    words = text.split()

    for word in words:
        word = word.lower()  # Optional: to make the count case-insensitive
        word_count[word] = word_count.get(word, 0) + 1

    return word_count
