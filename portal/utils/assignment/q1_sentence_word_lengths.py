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

    new_dict = dict()
    words = sentence.split()

    for word in words:
        word_lower = word.lower()
        new_word = ""
        for i in word_lower:
            if i.isalnum(): #checks if there is any punctution or not proceeds if not a punctuation
                new_word += i
        new_dict[new_word] = len(new_word) #assigns the word as key and its len as the value
    return new_dict

