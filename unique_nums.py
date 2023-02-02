#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:03:20 2023

@author: jamesboot
"""

def singleNumber(nums):
    
    value = 0
    
    for i in range(len(nums)):
        
        nums2 = nums[:]
        
        del nums2[i]
        
        if nums[i] not in nums2:
            
            value = nums[i]
    
    return value

test1 = [2,2,1]
test2 = [4,1,2,1,2]
test3 = [1]
test4 = [1,2,3,4,5,6,1,2,3,4,5,6,777,8,8,7,7,9,9,10,10,11,12,11,12]

singleNumber(test4)

