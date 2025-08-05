#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 3/4 - 1/2")

    def test_inheritance(self):
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)

if __name__ == '__main__':
    unittest.main()

