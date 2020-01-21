#!/usr/bin/python3
def read_file(filename=""):
    """read a text file and print it"""
    with open('my_file_0.txt', encoding='UTF-8') as f:
        print(f.read(), end='')
