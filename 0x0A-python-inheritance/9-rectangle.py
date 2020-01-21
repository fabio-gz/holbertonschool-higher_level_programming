#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        s = '[Rectangle] '
        return s + '{}/{}'.format(self.__width, self.__height)
