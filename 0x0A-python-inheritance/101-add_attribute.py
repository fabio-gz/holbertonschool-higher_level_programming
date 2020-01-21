#!/usr/bin/python3
def add_attribute(obj, attrib, value):
    """ adds a new attribute to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attrib, value)
    else:
        raise TypeError('can\'t add new attribute')
