#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argv = sys.argv[1:]
    lenght = len(argv)

    if lenght == 0:
        print('0 arguments.')
    elif lenght == 1:
        print('{:d} argument:'.format(lenght))
        print('{:d}: {:s}'.format(lenght, sys.argv[1]))
    elif lenght > 1:
        print('{:d} arguemnts:'.format(lenght))
        for i in range(len(argv)):
            print('{:d}: {:s}'.format(i + 1, sys.argv[i + 1]))
