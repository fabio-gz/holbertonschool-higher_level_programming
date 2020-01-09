#!/usr/bin/python3
class Square:
    """class for the area of square"""
    def __init__(self, size=0):
        """initial function for square
        Args:
             size: size fo square(int)
        """
        self.__size = size

    @property
    def size(self):
        """getter func to retieve size
        Return: returns size
        """
        return self.__size

    @size.setter
    def size(self, size=0):
        """setter func to checl for errors
        Args:
            size: square size
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
