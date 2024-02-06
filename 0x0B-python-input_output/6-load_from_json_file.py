#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json
import os

def load_from_json_file(filename):
    """create an object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    print(load_from_json_file("example.json"))  # Example usage

# Ensure the file ends with a newline character
print()
