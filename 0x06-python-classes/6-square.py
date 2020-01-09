#!/usr/bin/python3
class Square:
    """class for the area of square"""
    def __init__(self, size=0, position=(0, 0)):
        """initial function for square
        Args:
            size: size fo square(int)
            position: tuple position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gives position to print"""
        return self.__position

    @position.setter
    def position(self, value):
        """checks for bad code
        Args:
            value: tuple value for position
        """
        if not isinstance(value, tuple):
            if (value[0] < 0 and value[1] < 0):
                raise TypeError('position must be a tuple\
                of 2 positive integers')
        else:
            self.__position = position


    def area(self):
        """function to calculate square area
        Returns:
            returns the area calcualted
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints to de stdout the character '#'"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
