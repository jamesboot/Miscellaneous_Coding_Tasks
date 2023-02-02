#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:51:30 2023

@author: jamesboot
"""

# Given a roman numeral, convert it to an integer.
# https://leetcode.com/problems/roman-to-integer/


def romanToInt(s):
    
    lookup = {'I' : 1,
              'V' : 5,
              'X' : 10,
              'L' : 50,
              'C' : 100,
              'D' : 500,
              'M' : 1000}
    
    total = 0
    
    for x in range(len(s)):
        
        val = lookup[s[x]]
        nextPos = x+1
        
        if nextPos < len(s):
            
            nextVal = lookup[s[nextPos]]
        
            if val < nextVal:
                total -= val
            
            else:
                total += val
        
        else:
            total += val
            
    return total

romanToInt('MCMXCIV')





