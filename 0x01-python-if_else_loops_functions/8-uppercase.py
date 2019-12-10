#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= 97 and j <= 122:
            n = j - 32
        else:
            n = j

        print('{:c}'.format(n), end='')
    print('')
