#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a file
"""

import sys
import json
from os import path

# Load custom functions
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Name of the file to save the list
FILE_NAME = 'add_item.json'


def main():
    """Main function to handle argument adding and file saving"""
    # If the file doesn't exist, create an empty list
    if not path.exists(FILE_NAME):
        args_list = []
    else:
        # Load existing list from file
        args_list = load_from_json_file(FILE_NAME)

    # Append all arguments to the list
    args_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(args_list, FILE_NAME)


if __name__ == "__main__":
    main()
