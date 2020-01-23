#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    words = ''
    with open(filename, 'r+', encoding='UTF-8') as f:
        for i in f:
            words += i
            if search_string in i:
                words += new_string
        f.seek(0)
        f.write(words)
