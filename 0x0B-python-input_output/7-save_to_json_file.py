#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file sing JSON"""
    with open(filename, mode='w', encoding='UTF-8') as f:
        return f.write(json.dumps(my_obj))
