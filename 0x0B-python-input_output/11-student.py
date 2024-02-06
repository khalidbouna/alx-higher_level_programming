#!/usr/bin/python3
"""
Defines a Student class
"""

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    import sys
    import json

    # Check if filename is provided as argument
    if len(sys.argv) != 2:
        print("Usage: ./11-main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    # Save JSON representation to file
    with open(filename, 'w') as f:
        json.dump(j_student_1, f)

    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    # Load dictionary from file
    with open(filename, 'r') as f:
        new_j_student_1 = json.load(f)

    new_student_1.reload_from_json(new_j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
