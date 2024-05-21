#!/usr/bin/python3
"""
This module defines a class called Square.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
