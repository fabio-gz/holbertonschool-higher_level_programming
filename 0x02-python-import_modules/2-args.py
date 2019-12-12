#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argv = sys.argv[1:]
    lenght = len(argv)

    if lenght == 0:
        print('0 arguments.')
    elif lenght == 1:
        print('{} argument:'.format(lenght))
        print('{}: {:s}'.format(lenght, sys.argv[1]))
    elif lenght > 1:
        print('{} arguments:'.format(lenght))
        for i in range(len(argv)):
            print('{}: {:s}'.format(i + 1, sys.argv[i + 1]))
