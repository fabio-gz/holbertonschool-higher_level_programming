#!/usr/bin/python3
"""
class that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionary representation os Student"""
        d = {}
        if attrs is None:
            d = self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__[i]
        return d
