#!/usr/bin/python3
"""
Base class for all the other classes in this project
"""
import json
import csv


class Base:
    """Base clase for figures
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initial function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes de json representation of lists_objs
        """
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
        """returns the list of the json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an insrance with all attributes already set
        """
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
        ''' return a list of instances
        '''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r', encoding='UTF-8') as f:
                r1 = cls.from_json_string(f.read())
                return [cls.create(**args) for args in r1]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        filename = cls.__name__ + '.csv'
        lclass = []
        values = []
        classes = 0
        for i in range(len(list_objs)):
            values.append([])
            d = list_objs[i].to_dictionary()
            if classes == 0:
                for j in d:
                    lclass.append(j)
                classes = 1
        with open(filename, mode='w', newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=lclass)

            writer.writeheader()
            for i in range(len(list_objs)):
                d = list_objs[i].to_dictionary()
                writer.writerow(d)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize in csv"""
        filename = cls.__name__ + '.csv'
        d_csv = {}
        lvalues = []
        try:
            with open(filename, mode='r', encoding='UTF-8') as f:
                reader = csv.DictReader(f)
                for i in reader:
                    for j in i:
                        d_csv[j] = int(i[j])
                    lvalues.append(cls.create(**d_csv))
                return lvalues
        except:
            return lvalues
