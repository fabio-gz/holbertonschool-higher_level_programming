#!/usr/bin/python3
import json
"""
Base class for all the other classes in this project
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """initial function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes de json representation of lists_objs"""
        list1 = []
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                f.write(str(list1))
            else:
                for i in list_objs:
                    list1.append(cls.to_dictionary(i))

                f.write(cls.to_json_string(list1))
