#!/usr/bin/python3
def inherits_from(obj, a_class):
    """checks if an obj is instance of a class that inherited from the specified
    class"""
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
