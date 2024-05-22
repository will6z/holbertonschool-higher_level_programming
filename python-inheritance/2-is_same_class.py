#!/usr/bin/python3
"""
makin a function that returns true if the obj is the same instance
as the specified class
"""


def is_same_class(obj, a_class):
    """
    returns the type() of obj and compares to a_class
    Args:
        obj
        a_class
    """
    return type(obj) is a_class
