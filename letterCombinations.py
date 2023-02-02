#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:39:46 2023

@author: jamesboot
"""

# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

def letterCombinations(digits):
    
    lookup = {2 : 'abc',
              3 : 'def',
              4 : 'ghi',
              5 : 'jkl',
              6 : 'mno',
              7 : 'pqrs',
              8 : 'tuv',
              9 : 'wxyz'}
        
    if len(digits) == 0:
        return []
    
    elif len(digits) == 1:
        intDigits = int(digits)
        return list(lookup[intDigits])
    
    elif len(digits) == 2:
        combs = []
        digit1 = int(digits[0])
        digit2 = int(digits[1])
        
        for i in range(len(lookup[digit1])):
            
            for j in range(len(lookup[digit2])):
                letters = lookup[digit1][i] + lookup[digit2][j]
                combs.append(letters)
        
        return combs
    
    elif len(digits) == 3:
        combs = []
        digit1 = int(digits[0])
        digit2 = int(digits[1])
        digit3 = int(digits[2])
        
        for i in range(len(lookup[digit1])):
            
            for j in range(len(lookup[digit2])):
                
                for k in range(len(lookup[digit3])):
                    letters = lookup[digit1][i] + lookup[digit2][j] + lookup[digit3][k]
                    combs.append(letters)
        
        return combs
    
    elif len(digits) == 4:
        combs = []
        digit1 = int(digits[0])
        digit2 = int(digits[1])
        digit3 = int(digits[2])
        digit4 = int(digits[3])
        
        for i in range(len(lookup[digit1])):
            
            for j in range(len(lookup[digit2])):
                
                for k in range(len(lookup[digit3])):
                    
                    for l in range(len(lookup[digit4])):
                        letters = lookup[digit1][i] + lookup[digit2][j] + lookup[digit3][k] + lookup[digit3][l]
                        combs.append(letters)
        
        return combs


print(letterCombinations('2593'))

