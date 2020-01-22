#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns number of lines in the file"""
    with open(filename, encoding='UTF-8') as f:
        lineNum = 0
        while True:
            line = f.readline()
            if not line:
                break
            lineNum += 1

        return lineNum
