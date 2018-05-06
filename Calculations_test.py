# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:14:57 2018
test_Calculations.py
C:\users\pk\desktop\pythoncode>python -m unittest Calculations_test.py
@author: dongrp2
"""
import unittest
import Calculations

class TestCalculations(unittest.TestCase):
    
    def test_add(self):
        result = Calculations.add(10,5)
        self.assertEqual(result, 15)