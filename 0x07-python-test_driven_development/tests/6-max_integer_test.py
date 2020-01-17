#!/usr/bin/python3
"""
test for max_integer

"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_maxintlist(self):
        """test for a list of ints"""
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_maxunord_list(self):
        """test on an unordered list"""
        self.assertEqual(max_integer([7, 5, 3, 9, 2]), 9)

    def test_neg_list(self):
        """test for a negative list"""
        self.assertEqual(max_integer([-6, -3, -1, -5]), -1)

    def test_float_list(self):
        """test a list of floats"""
        self.assertEqual(max_integer([3.3, 2.1, -3.9]), 3.3)

    def test_empty_list(self):
        """test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_str_list(self):
        """test a list of str"""
        self.assertEqual(max_integer(['hola', 'zoe', 'luna']), 'zoe')

    def test_mul_type(self):
        """test a list of multiple types"""
        with self.assertRaises(TypeError):
            max_integer(['3', 4, 'hello'])

    def test_none_list(self):
        """test a list with argument none"""
        with self.assertRaises(TypeError):
            max_integer(None)
