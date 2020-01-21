#!/usr/bin/python3
def class_to_json(obj):
    """returns a dictionary description"""
    d = obj.__dict__
    return d
