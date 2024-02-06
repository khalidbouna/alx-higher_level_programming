#!/usr/bin/python3
"""
Creates an Object from a “JSON file”.
"""

def load_from_json_file(filename):
    """Creates an object from filename (JSON file)."""
    import json
    with open(filename, 'r') as file:
        return json.load(file)
