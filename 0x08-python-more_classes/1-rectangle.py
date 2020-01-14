#!/usr/bin/python3
class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """define the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """define the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__height = value
