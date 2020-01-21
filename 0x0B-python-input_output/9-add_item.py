#!/usr/bin/python3
"""
adds argument to a Python list
"""
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_file = load_from_json_file("add_item.json")
except:
    my_file = []

for i in range(1, len(sys.argv)):
    my_file.append(sys.argv[i])

save_to_json_file(my_file, "add_item.json")
