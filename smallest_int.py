#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:11:27 2023

@author: jamesboot
"""

# Given an array (A) of N integers return the smallest positive integer
# That does not occur in A

def solution(A):
    
    # Create a set of all the numbers in A
    num_set = set(A)
    
    # Find the smallest number in the set
    smallest = min(num_set)
    
    # if the smallest value is less than 0 start from 1
    if smallest < 0:
        
        smallest = 1
        
        while smallest in num_set:
            
            smallest += 1
    
    else:
        
        while smallest in num_set:
            
            smallest += 1
    
    return smallest

solution([-1, -2])