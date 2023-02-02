#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:18:58 2023

@author: jamesboot
"""

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

def majorityElement(nums):
    
    target = len(nums)/2
    
    count = 0
    
    returnValue = 0
    
    for i in range(len(nums)):
        
        number = nums[i]
        
        for j in range(len(nums)):
            
            if number == nums[j]:
                
                count += 1
                
        if count > target:
            
            returnValue = number
            
    return returnValue

test1 = [3,2,3]
test2 = [2,2,1,1,1,2,2]

majorityElement(test2)

