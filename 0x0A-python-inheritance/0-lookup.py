#!/usr/bin/python3
def lookup(obj):
    """returns a list of available attributes and methods"""
    l = (dir(obj))
    return l
