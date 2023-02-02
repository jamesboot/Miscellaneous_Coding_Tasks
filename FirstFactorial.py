#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:49:44 2023

@author: jamesboot
"""

# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
# For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
# For the test cases, the range will be between 1 and 18 and the input will always be an integer.

def FirstFactorial(num):
  
  # code goes here
  fact = num-1

  while fact > 0:
    num = num*fact
    fact -= 1

  return num

# keep this function call here 
FirstFactorial(4)

