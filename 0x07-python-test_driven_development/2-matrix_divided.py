#!/usr/bin/python3
"""

    Divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """ function to divide all elements of the matrix by div
    Args:
        matrix: a list of list
        div: number greater than zero
    Returns:
        A new list of list with the operation made
    """
    i = 0
    j = 0
    if not isinstance(matrix, list) or len(matrix) == 0 or\
       not all(isinstance(i, list) for i in matrix) or not\
       isinstance(matrix[i][j], (int, float)):
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    trix = [[round(j / div, 2) for j in i] for i in matrix]
    return trix
