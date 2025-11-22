"""Assignment Q10 - Find Anagrams

Write a function that finds all anagrams of a given word from a list of words.

An anagram is a word formed by rearranging the letters of another word.

Example:
    >>> q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"])
    ['silent', 'enlist']
"""


def q10_find_anagrams(word, word_list):
    """
    Finds all anagrams of a given word from a list of words.
    
    An anagram is a word formed by rearranging the letters of another word.
    
    Args:
        word (str): The word to find anagrams for
        word_list (list): A list of words to search
        
    Returns:
        list: A list of anagrams found in word_list
        
    Example:
        >>> q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"])
        ['silent', 'enlist']
    """
    anagram = []
    for i in word_list:
        if sorted(i) == sorted(word) and i != word: #sorted is an inbuilt function which takes a word and sorts it alphabetically
            anagram.append(i)
    return anagram