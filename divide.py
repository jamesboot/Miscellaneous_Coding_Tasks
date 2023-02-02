#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:27:14 2023

@author: jamesboot
"""

# Given two integers dividend and divisor, 
# divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within 
# the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
# For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, 
# and if the quotient is strictly less than -2^31, then return -2^31.

def divide(dividend, divisor):
    
    if divisor < 0 and dividend > 0:
        
        divisorNew = abs(divisor)
        
        quotient = 0
        
        while divisorNew <= dividend:
            quotient += 1
            divisorNew += abs(divisor)
    
        if quotient > 2**31:
            return -2**31
        
        else:
            return -abs(quotient)
        
    if divisor > 0 and dividend < 0:
        
        divisorNew = abs(divisor)
        
        dividendNew = abs(dividend)
        
        quotient = 0
        
        while divisorNew <= dividendNew:
            quotient += 1
            divisorNew += abs(divisor)
    
        if quotient > 2**31:
            return -2**31
        
        else:
            return -abs(quotient)
    
    if divisor > 0 and dividend > 0:
        
        divisorNew = abs(divisor)
        
        quotient = 0
        
        while divisorNew <= dividend:
            quotient += 1
            divisorNew += abs(divisor)
        
        if quotient > (2**31)-1:
            return (2**31)-1
        
        else:
            return quotient
    
    if divisor < 0 and dividend < 0:
        
        divisorNew = abs(divisor)
        
        quotient = 0
        
        while divisorNew <= dividend:
            quotient += 1
            divisorNew += abs(divisor)
        
        if quotient > (2**31)-1:
            return (2**31)-1
        
        else:
            return quotient
        
    if abs(dividend) < abs(divisor):
        return 0

print(divide(10, 3))
print(divide(7, -3))
print(divide(-7, 3))
print(divide(3, 7))
print(divide(-3, -7))
print(divide(3, -7))
print(divide(-3, 7))
print(divide(27, 9))
print(divide(7868, 9))
print(divide(2**33, 1))
print(divide(982374, 73))






