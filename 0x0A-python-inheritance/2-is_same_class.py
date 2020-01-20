#!/usr/bin/python3
def is_same_class(obj, a_class):
    """checks if an object is an instance of a class
    Args:
        obj: object to check
        a_class: class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
