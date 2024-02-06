#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """Reads filename and prints its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
