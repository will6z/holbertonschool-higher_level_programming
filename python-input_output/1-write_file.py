#!/usr/bin/python3
"""
func that appends to a file
"""


def append_write(filename="", text=""):
    """
    allowing func permission append = 'a'
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
