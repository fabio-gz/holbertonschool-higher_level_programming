#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
