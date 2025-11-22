"""Assignment Q8 - Remove Duplicates

Write a function that takes a list and returns a new list with duplicates removed, 
preserving the original order.

Example:
    >>> q8_remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    [1, 2, 3, 4, 5]
"""


def q8_remove_duplicates(items):
    """
    Takes a list and returns a new list with duplicates removed, 
    preserving the original order.
    
    Args:
        items (list): The input list
        
    Returns:
        list: A new list with duplicates removed, in original order
        
    Example:
        >>> q8_remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    new_list = []

    for i in items: #loops through all the numbers in the list
        if i not in new_list:
            new_list.append(i)
    return new_list

