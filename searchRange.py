#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:09:20 2023

@author: jamesboot
"""

# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

def searchRange(nums, target):
    
    positions = []
    
    for x in range(len(nums)):
        
        if nums[x] == target:
            positions.append(x)
    
    if len(positions) >= 2:
        
        return [positions[0], positions[-1]]
    
    else:
        return [-1, -1]

nums = []
target = 6

print(searchRange(nums, target))



