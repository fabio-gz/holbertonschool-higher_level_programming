#!/usr/bin/python3
class Square:
    """class for the area of square"""
    def __init__(self, size=0, position=(0, 0)):
        """initial function for square
        Args:
            size: size fo square(int)
            position: tuple position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter func to retieve size
        Return: returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter func to checl for errors
        Args:
            size: square size
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """gives position to print
        Return:
            retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """checks for bad code
        Args:
            value: tuple value for position
        """
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0 or\
           len(value) != 2 or not isinstance(value[0], int) or not\
                isinstance(value[1], int):
            raise TypeError('position must be a tuple'
                            ' of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """function to calculate square area
        Return:
            returns the area calcualted
        """
        return (self.__size) ** 2

    def __str__(self):
        """prints a square"""
        new_print = ''
        if self.__size == 0:
            return new_print
        for i in range(self.position[1]):
            new_print += '\n'
        for j in range(self.__size):
            new_print += self.position[0] * ' '
            new_print += self.__size * '#'
            if j != self.__size - 1:
                new_print += '\n'
        return new_print

    def my_print(self):
        """prints to de stdout the character '#'"""
        if self.__size == 0:
            print('')
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
