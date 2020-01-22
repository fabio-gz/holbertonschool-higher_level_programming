#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read a text file and print it
    Args:
        filename: text file
        nb_lines: lines to read
    """
    with open(filename, encoding='UTF-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        for i in range(0, nb_lines):
            print(f.readline(), end='')
