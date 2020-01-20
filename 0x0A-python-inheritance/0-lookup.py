#!/usr/bin/python3
def lookup(obj):
    """returns a list of available attributes and methods"""
    l = list(dir(obj))
    return l
