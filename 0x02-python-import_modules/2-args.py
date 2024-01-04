#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    count = len(sys.argv) - 1

    print(f"{count} {'argument' if count == 1 else 'arguments'}:")
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
