#!/usr/bin/python3
"""
Defines the Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initializes a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
