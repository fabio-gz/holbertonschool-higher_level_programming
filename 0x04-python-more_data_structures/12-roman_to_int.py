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

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    first = 0
    last = 0
    res = 0
    n = []

    for letter in roman_string:
        n.append(ROMAN.get(letter))

    if len(n) == 1:
        return n[0]

    for first, last in zip(n, n[1:]):
        if first < last:
            res = res - first
        else:
            res = res + first

    return res + last
