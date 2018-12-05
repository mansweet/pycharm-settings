#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michael Mansour; (michael_mansour@symamtec.com)'

import unittest
import os

os.environ['UNITTESTING'] = '1'

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
