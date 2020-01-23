#!/usr/bin/python3
def pascal_triangle(n):
    list1 = []
    l_c = []

    for i in range(0, n):
        p = list1

        if i is not 0:
            list1 = [1]
        for j in range(1, i):
            list1.append(p[j - 1] + p[j])
        list1.append(1)
        l_c.append(list1)
    return l_c
