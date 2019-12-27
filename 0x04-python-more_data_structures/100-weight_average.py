#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        x = sum(i[0] * i[1] for i in my_list)
        y = sum(j[1] for j in my_list)
    else:
        return 0
    return (x / y)
