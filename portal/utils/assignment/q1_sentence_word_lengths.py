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
    
    dictionary2 = {}
    
    words = sentence.split()

    
    for i in words:
    
        if i in dictionary2:
          
            dictionary2[i] += 1
        else:
           
            dictionary2[i] = 1

    return dictionary2
    