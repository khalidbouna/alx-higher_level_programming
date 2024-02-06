#!/usr/bin/python3
"""
Defines a Student class with public instance attributes and a to_json method
"""

class Student:
    """
    Student class to represent a student with first name, last name, and age
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with given first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
