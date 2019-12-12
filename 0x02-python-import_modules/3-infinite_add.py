#!/usr/bin/python3
import sys


def i_add():
    nums = sys.argv[1:]
    sums = 0

    for i in nums:
        sums = sums + int(i)

    print('{}'.format(sums))

if __name__ == "__main__":
    i_add()
