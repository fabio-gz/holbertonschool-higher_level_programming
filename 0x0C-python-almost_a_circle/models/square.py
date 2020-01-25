#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initial for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """check for size errors"""
        self.width = value
        self.height = value

    def __str__(self):
        """str for print"""
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                  self.y, self.size))

    def update(self, *args, **kwargs):
        """implementation of args and kwargs"""
        attr = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
