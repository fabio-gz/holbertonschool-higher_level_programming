#!/usr/bin/pyhton3
def complex_delete(a_dictionary, value):
    {a_dictionary.pop(i) for i in list(a_dictionary)
     if a_dictionary[i] == value}
    return a_dictionary
