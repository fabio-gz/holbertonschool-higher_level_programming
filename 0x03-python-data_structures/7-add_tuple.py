#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (tuple_a + (0, 0))
    tuple_b = (tuple_b + (0, 0))
    for i, j in zip(tuple_a, tuple_b):
        res = [i + j, tuple_a[i] + tuple_b[i]]
        return tuple(res[:2])
