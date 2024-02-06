#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
