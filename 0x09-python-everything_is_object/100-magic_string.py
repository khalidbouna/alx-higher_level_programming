#!/usr/bin/python3
def magic_string(H=None):
    if H is None:
        H = ["BestSchool"]
    else:
        H.append("BestSchool")
    return ", ".join(H)
