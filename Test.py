#!/usr/bin/python3

import unittest

from Subtraction import Diff
from Division import Quot

class Maths(unittest.TestCase):

    def test_Subtraction(self):
        diff = Diff(10, 10)
        self.assertEqual(diff, 10)

    def test_Division(self):
        div = Quot(10, 10)
        self.assertEqual(div, 2)

if __name__ == '__main__':
    unittest.main()
