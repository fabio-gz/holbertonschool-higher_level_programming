#!/usr/bin/python3
"""
Test for base class
"""
import unittest
import pep8
from models.base import Base


class test_base(unittest.TestCase):
    """tester for base class"""

    def setUp(self):
        """run method prior test"""
        Base._Base__nb_objects = 0

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

    def Testpep8(self):
        """test for pep8 styleguide"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py',
                                        'models/base.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')
