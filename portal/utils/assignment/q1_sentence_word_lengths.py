"""Assignment Q1 - Sentence Word Lengths

Write a function that takes a sentence and returns a dictionary mapping each word to its length.

- Ignore punctuation.
- Treat words case-insensitively.

Example:
    >>> q1_sentence_word_lengths("Hello, World!")
    {'hello': 5, 'world': 5}
"""


def q1_sentence_word_lengths(sentence):
    """
    Takes a sentence and returns a dictionary mapping each word to its length.
    
    - Ignore punctuation.
    - Treat words case-insensitively.
    
    Args:
        sentence (str): The input sentence to analyze
        
    Returns:
        dict: A dictionary where keys are words (lowercase) and values are their lengths
        
    Example:
        >>> q1_sentence_word_lengths("Hello, World!")
        {'hello': 5, 'world': 5}
    """

    dict2 = {}
    
    words = sentence.split()  # split the sentence into words

    for word in words:
        # convert to lowercase
        word_lower = word.lower()
        
        # remove punctuation manually
        clean_word = ""
        for char in word_lower:
            if char.isalnum():  # keep only letters and numbers
                clean_word += char

        # store the length of the word in the dictionary
        dict2[clean_word] = len(clean_word)
    
    return dict2

