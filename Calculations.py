# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:58:01 2018
Calculation
@author: dongrp2
"""

def add(a,b):
    return a + b
#print(add(10,5))
    
def sub(a,b):
    return a - b
#print(sub(10,5))

def mul(a,b):
    return a * b
#print(mul(10,5))
    
def div(a,b):
    if b == 0:
        raise ValueError("Can not divide by zero!")
    return a / b
#print(div(10,10))