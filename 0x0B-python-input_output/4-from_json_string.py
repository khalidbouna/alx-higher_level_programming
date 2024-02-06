#!/usr/bin/python3
"""
Returns an object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    """Returns the Python data structure represented by my_str."""
    import json
    return json.loads(my_str)
