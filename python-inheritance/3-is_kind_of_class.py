#!/usr/bin/python3
"""
Writing a function that returns True if the object is an instance of, or if the object is an 
instance of a class that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Checking if the obj is an instance

    Args:
        obj
        a_class
    Returns:
        True if obj is an instance of inherited from a_class
    """
    return isinstance(obj, a_class)
