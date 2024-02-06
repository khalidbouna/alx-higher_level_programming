#!/usr/bin/python3
"""
Defines the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
