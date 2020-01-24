#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """class for Square construction"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print func"""
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                  self.y, self.height))
