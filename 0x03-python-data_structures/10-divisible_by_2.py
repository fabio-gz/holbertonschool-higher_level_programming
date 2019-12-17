#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mod2 = []
    for i in my_list:
        if i % 2 == 0:
            mod2.append(True)
        else:
            mod2.append(False)
    return mod2
