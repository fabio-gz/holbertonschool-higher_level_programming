#!/usr/bin/python3
"""
Test for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """test cases for class Rectangle"""

    def setUp(self):
        """run method prior test"""
        Base._Base__nb_objects = 0

    def test_twoargs(self):
        """test for two args"""
        r2 = Rectangle(1, 2)
        self.assertEqual((r2.id), 1)

    def test_completargs(self):
        """test for complete args array"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r1.id), 12)

    def test_moreargs(self):
        """test for more args than allowed"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_areafunc(self):
        """test for the area function"""
        r1 = Rectangle(5, 5)
        self.assertEqual((r1.area()), 25)
