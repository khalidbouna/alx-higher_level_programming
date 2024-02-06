#!/usr/bin/python3
"""
Defines the MyList class.
"""


class MyList(list):
    """A subclass of list with additional functionality."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
