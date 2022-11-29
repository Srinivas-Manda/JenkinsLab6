#!/usr/bin/python3

import unittest

from Subtraction import Diff
from Task2 import Quot

class Maths(unittest.TestCase):

    def test_Subtraction(self):
        diff = Diff(20, 10)
        self.assertEqual(diff, 30)

    def test_Division(self):
        div = Quot(20, 10)
        self.assertEqual(div, 200)

if __name__ == '__main__':
    unittest.main()
