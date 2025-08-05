#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

if __name__ == '__main__':
    unittest.main()

