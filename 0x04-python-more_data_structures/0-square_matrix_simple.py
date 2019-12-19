#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sub_matrix = []
        new_matrix.append(sub_matrix)
        for j in i:
            sub_matrix.append(j ** 2)
    return new_matrix
