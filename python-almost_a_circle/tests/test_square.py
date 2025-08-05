#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_str(self):
        s = Square(5, 1, 2, 88)
        self.assertEqual(str(s), "[Square] (88) 1/2 - 5")

    def test_inheritance(self):
        s = Square(4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)

    def test_area(self):
        s = Square(6)
        self.assertEqual(s.area(), 36)

if __name__ == '__main__':
    unittest.main()

