#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import sys
import requests

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
