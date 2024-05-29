#!/usr/bin/python3

"""
makin a func that writes a string to a txt file
"""


def write_file(filename="", text=""):

    """
    func adds a string to a txt. file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
