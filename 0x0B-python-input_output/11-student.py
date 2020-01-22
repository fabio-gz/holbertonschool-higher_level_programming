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

    def to_json(self):
        """retrieve a dictionary representation os Student"""
        return self.__dict__
