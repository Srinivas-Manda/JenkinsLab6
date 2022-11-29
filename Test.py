#!/usr/bin/python3

import unittest

from Subtraction import Diff
from Division import Quot

class Maths(unittest.TestCase):

    def test_Subtraction(self):
        diff = Diff(50, 10)
        self.assertEqual(diff, 30)

    def test_Division(self):
        div = Quot(30, 10)
        self.assertEqual(div, 3)

if __name__ == '__main__':
    unittest.main()
