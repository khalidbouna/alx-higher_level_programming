#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
