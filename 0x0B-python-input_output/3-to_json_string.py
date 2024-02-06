#!/usr/bin/python3
"""
Returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj."""
    import json
    return json.dumps(my_obj)
