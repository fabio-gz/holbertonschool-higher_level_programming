#!/usr/bin/python3
class Square:
    """class for the area of square"""
    def __init__(self, size=0):
        """initial function for square
        Args:
             size: size fo square(int)
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """function to calculate square area
        Returns:
            returns the area calcualted
        """
        return (self.__size) ** 2
