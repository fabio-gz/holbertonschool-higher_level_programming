#!/usr/bin/python3
"""
Parent class BaseGeometry to handle forms
"""


class BaseGeometry:
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        s = '[Rectangle] '
        return s + '{}/{}'.format(self.__height, self.__width)


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)
