#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:31:46 2023

@author: jamesboot
"""

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3^x.

import math

def isPowerOfThree(n):
    
    # Solve equation for X and test if X is an integer
    
    if n <= 1:
        
        return False
    
    elif math.log(n, 3).is_integer():
        
        return True
    
    else:
        
        return False

print(isPowerOfThree(9))
print(isPowerOfThree(7))
print(isPowerOfThree(21))
print(isPowerOfThree(27))
print(isPowerOfThree(81))
print(isPowerOfThree(1))
print(isPowerOfThree(-1))
print(isPowerOfThree(-34567))

3**234

print(isPowerOfThree(4429692754456178336783573163941511542801609124865708991796231237006094959798985924070291617478620287394759702569))



