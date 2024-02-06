#!/usr/bin/python3
""" class_to_json module
"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return obj.__dict__.copy()
