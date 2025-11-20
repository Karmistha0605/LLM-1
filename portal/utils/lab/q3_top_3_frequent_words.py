"""W1D1 Q3 - Top 3 Frequent Words

Return the top 3 most frequent words in a string.

Example:
    >>> q3_top_3_frequent_words("the cat and the dog and the bird")
    [('the', 3), ('and', 2), ('cat', 1)]
"""


def q3_top_3_frequent_words(text):
    """
    Return the top 3 most frequent words in a string.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        list: A list of tuples containing (word, frequency) for the top 3 most frequent words
        
    Example:
        >>> q3_top_3_frequent_words("the cat and the dog and the bird")
        [('the', 3), ('and', 2), ('cat', 1)]
    """
    word = text.split()
    frequency = {}

    for i in word:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    
    top = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3] #first change the dictionary into list //Lambla x (is each tuple) x:[1] requests the index 1 that is the frequency 
     
    return top
