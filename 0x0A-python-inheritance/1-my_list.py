#!/usr/bin/python3
"""

class to print a sorted list

"""


class MyList(list):
    """prints a sorted list"""
    def print_sorted(self):
        print(sorted(self))
