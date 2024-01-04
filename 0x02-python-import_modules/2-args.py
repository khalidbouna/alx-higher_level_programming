#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        print(f"Number of argument{'s' if count != 1 else ''}: {count}{'.' if count == 0 else ''}")

        for i in range(1, count + 1):
            print(f"{i}: {sys.argv[i]}")
