#!/usr/bin/python3
"""
class for rebel MyInt
"""


class MyInt(int):
    def __ne__(self, i):
        return True

    def __eq__(self, i):
        return False
