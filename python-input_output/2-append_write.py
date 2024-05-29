#!/usr/bin/python3
"""
makin a func that appends a string to the end of a txt file
"""


def append_write(filename="", text=""):
    """
    func appends a string at the end of a txt file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
