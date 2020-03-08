#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])
        
    def test_setitem(self):
        a = Vector([0, 1, 2, 3])
        a.__setitem__(1, 10)
        
        self.assertEqual(a.__getitem__(1), 10)
        
    def test_cmp(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([0, 1, 2, 3])
        self.assertEqual(a.__cmp__(b), 0)
        
        a.__setitem__(1, 10)
        self.assertEqual(a.__cmp__(b), 1)
        
        b.__setitem__(1, 11)
        self.assertEqual(a.__cmp__(b), -1)
        
    def test_neg(self):
        a = Vector([0, 1, 2, 3])
        self.assertEqual(a.__neg__().get(), [0, -1, -2, -3])
        
    def test_reversed(self):
        a = Vector([0, 1, 2, 3])
        self.assertEqual(a.__reversed__().get(), [3, 2, 1, 0])
        
    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([1, 2])
        self.assertEqual(a.__sub__(b).get(), [0,3])
    
    def test_mul(self):
        a = Vector([0, 1, 2, 3])
        self.assertEqual(a.__mul__(10).get(), [0,10,20,30])
        
    def test_xor(self):
        a = Vector([0, 1, 2, 3])
        self.assertEqual(a.__xor__(2).get(), [2,3,0,1])
        
        
        
        
        



if __name__ == "__main__":
    unittest.main()  # pragma: no cover
