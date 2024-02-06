#!/usr/bin/python3
"""
Writes an Object to a text file using a JSON representation.
"""

def save_to_json_file(my_obj, filename):
    """Writes my_obj to filename using JSON representation."""
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
