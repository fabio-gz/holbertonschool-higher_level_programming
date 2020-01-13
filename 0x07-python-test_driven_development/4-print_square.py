#!/usr/bin/python3
"""

print a square

"""


def print_square(size):
    """ function to print a square
    Args:
        size: integer, size of square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for i in range(0, size):
        print('#' * size)
