#!/usr/bin/python3
"""displays the value of the X-Request-Id variabl"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.info()
    print(header['X-Request-Id'])
