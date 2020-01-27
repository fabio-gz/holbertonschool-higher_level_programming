#!/usr/bin/python3

import json
"""
Base class for all the other classes in this project
"""


class Base:
    """Base clase for figures"""
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an insrance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == 'Square':
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ return a list of instances"""
        filename = cls.__name__ + '.json'
        list1 = []
        if filename is None:
            return '[]'
        else:
            with open(filename, encoding='UTF-8') as f:
                for arg in cls.from_json_string(f.read()):
                    list1.append(cls.create(**arg))
                return list1
