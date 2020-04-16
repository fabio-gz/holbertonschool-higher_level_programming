#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request """
import sys
import urllib.request

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        html = page.decode('utf-8')
        print(html)
