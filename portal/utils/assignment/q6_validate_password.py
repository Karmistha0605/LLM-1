"""Assignment Q6 - Validate Password

Write a function that checks if a password string meets the following conditions:

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- Return True if valid, False otherwise.

Example:
    >>> q6_validate_password("ValidPass123")
    True
    
    >>> q6_validate_password("weakpass")
    False
"""


def q6_validate_password(password):
    """
    Checks if a password string meets the following conditions:
    
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    
    Args:
        password (str): The password string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> q6_validate_password("ValidPass123")
        True
        
        >>> q6_validate_password("weakpass")
        False
    """
    upper = False # initializing the variable
    lower = False
    digit = False

    if len(password) < 8:
        return False
    
    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
    if upper and lower and digit: # if all the condition is true then only return a valid pass
        return True
    else:
        return False
