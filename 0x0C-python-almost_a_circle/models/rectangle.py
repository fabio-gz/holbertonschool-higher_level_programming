#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """class for Rectangle construction"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter func for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @width.setter
    def height(self, value):
        """setter func for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieve the x"""
        return self.__x

    @width.setter
    def x(self, value):
        """setter func for x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieve the x"""
        return self.y

    @width.setter
    def y(self, value):
        """setter func for x"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle taking care of x and y"""
        for j in range(self.__y):
            print('')
        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))
