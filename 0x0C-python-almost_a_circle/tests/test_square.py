#!/usr/bin/python3
"""
Test for Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):
    """test cases for class Square"""

    def test_twoargs(self):
        """test for two args"""
        s1 = Square(5, 6)
        self.assertEqual((s1.id), 1)

    def test_completearg(self):
        """test for complete args"""
        s1 = Square(10, 3, 4, 5)
        self.assertEqual((s1.id), 5)

    def test_moreargs(self):
        """test for more args than allowed"""
        with self.assertRaises(TypeError):
            s1 = Square(3, 4, 5, 7, 10, 11)

    def test_nonesquare(self):
        """test for no args provided"""
        with self.assertRaises(TypeError):
            s1 = Square()
