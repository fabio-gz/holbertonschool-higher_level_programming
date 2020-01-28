#!/usr/bin/python3
"""
Test for base class
"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """tester for base class"""

    def test_int(self):
        """test for one int"""
        b1 = Base(3)
        self.assertEqual((b1.id), 3)

    def test_negint(self):
        """test for negative int"""
        b1 = Base(-2)
        self.assertEqual((b1.id), -2)

    def test_noarg(self):
        """test for no args"""
        b1 = Base()
        self.assertEqual((b1.id), 1)

    def test_twoargs(self):
        """test for two args"""
        with self.assertRaises(TypeError):
            b1 = Base(2, 3)
