#!/usr/bin/python3
"""
Defines a Student class
"""

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
