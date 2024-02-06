#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
