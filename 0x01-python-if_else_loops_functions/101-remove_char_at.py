#!/usr/bin/python3
def remove_char_at(str, n):
    s1 = str[:n]
    s2 = str[n + 1:]
    return s1 + s2
