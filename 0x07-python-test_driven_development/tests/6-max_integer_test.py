#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test"""
    def test_onearg(self):
        self.assertEqual(max_integer([2]), 2)

    def test_negative(self):
        self.assertEqual(max_integer([-6, -3, -5, -1, -8]), -1)

    def test_negativepositive(self):
        self.assertEqual(max_integer([-83, -2, -4, 4, -2]), 4)

    def test_isNone(self):
        self.assertIsNone(max_integer([None]))

    def test_zero(self):
        self.assertEqual(max_integer([0]), 0)
