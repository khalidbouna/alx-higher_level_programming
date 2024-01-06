#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in range(-10, 11):
 if i > 0:
    print(i, "is positive")
 elif i < 0:
    print(i, "is negative")
 else:
    print(i, " zero")
