#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function to add two integers or floats after casting them to integers.
    
    Args:
        a: The first number, which must be an integer or a float.
        b: The second number, which must be an integer or a float, defaults to 98.
    
    Returns:
        The integer result of adding the two numbers.
    
    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both a and b to integers
    a = int(a)
    b = int(b)
    
    return a + b
