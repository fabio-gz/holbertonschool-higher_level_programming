#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= 65 or j <= 90:
            n = j
        else:
            n = j - 32

        print('{:c}'.format(n), end='')
    print('')
