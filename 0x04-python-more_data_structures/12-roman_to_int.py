#!/usr/bin/python3
def roman_to_int(roman_string):
    ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    n = []
    for key in ROMAN:
        for letter in roman_string:
            if letter in key:
                n.append(ROMAN.get(key))
            else:
                pass
    return sum(n)
