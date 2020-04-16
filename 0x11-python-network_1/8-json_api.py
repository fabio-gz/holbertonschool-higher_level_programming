#!/usr/bin/python3
""" sends a POST request with the letter as a parameter."""
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        response = r.json()
        if len(response) == 2:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
