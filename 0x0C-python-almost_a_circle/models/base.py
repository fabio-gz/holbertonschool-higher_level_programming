#!/usr/bin/python3
"""
Base class for all the other classes in this project
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """initial function"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
