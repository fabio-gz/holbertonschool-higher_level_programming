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
        """define the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__height = value

    def area(self):
        """return area of rectanlge"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """call-e print function"""
        str1 = ''
        if self.__height == 0 or self.__width == 0:
            return str1
        for i in range(self.__height):
            for j in range(self.__width):
                str1 += '#'
            if i < self.__height - 1:
                str1 += '\n'
        return str1

    def __repr__(self):
        str2 = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return str2
