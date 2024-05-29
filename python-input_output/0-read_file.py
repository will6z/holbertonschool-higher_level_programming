#!/usr/bin/python3
"""
makin a func that reads a txt. file
"""


def read_file(filename=""):
    """
    fun takes a filename and opens with open()
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
