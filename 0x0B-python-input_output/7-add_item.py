#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

import json
import sys
from os.path import exists

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    if exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for arg in sys.argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
