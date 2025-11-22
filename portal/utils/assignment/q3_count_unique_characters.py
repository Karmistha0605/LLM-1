"""Assignment Q3 - Count Unique Characters

Write a function that takes a string and returns the number of unique characters.

- Ignore spaces and case.

Example:
    >>> q3_count_unique_characters("Hello World")
    8
"""


def q3_count_unique_characters(text):
    """
    Takes a string and returns the number of unique characters.
    
    - Ignore spaces and case.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        int: The number of unique characters (ignoring spaces and case)
        
    Example:
        >>> q3_count_unique_characters("Hello World")
        8
    """
    count = 0
    a = []

    for char in text:
        if char != " " and char not in a: #only append into the list if not a space and if the character not already in a
            a.append(char)
            count +=1 #increase the count
    return count
