"""Assignment Q5 - Reverse Words

Write a function that takes a sentence and returns a new sentence with each word reversed, 
but the word order remains the same.

- Ignore punctuation.

Example:
    >>> q5_reverse_words("Hello, World!")
    "olleH, dlroW!"
"""


def q5_reverse_words(sentence):
    """
    Takes a sentence and returns a new sentence with each word reversed, 
    but the word order remains the same.
    
    - Ignore punctuation.
    
    Args:
        sentence (str): The input sentence
        
    Returns:
        str: A new sentence with each word reversed
        
    Example:
        >>> q5_reverse_words("Hello, World!")
        "olleH, dlroW!"
    """
    reversed_sentence = ""
    words = sentence.split()

    for word in words:
        letters_list = []
        for i in word:
            if i.isalpha():
                letters_list.append(i) #if i is a letter then only add to the list

        letters_list.reverse()
        new_word = ""
        index = 0

        for i in word:
            if i.isalpha():
                new_word += letters_list[index]
                index += 1
            else:
                new_word += i

        reversed_sentence += new_word + " "  

    return reversed_sentence