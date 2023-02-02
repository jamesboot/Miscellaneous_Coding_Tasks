#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:59:37 2023

@author: jamesboot
"""

# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

nums = [100,4,200,1,3,2]

def longestConsecutive(nums):
    
    allcounts = []
    
    sortNums = sorted(nums)
    
    for i in range(len(sortNums)):
        
        count = 0
        
        while sortNums[i]+1 == sortNums[i+1]:
            
            count += 1
            i += 1
        
        allcounts.append(count)
    
    return max(allcounts)

print(longestConsecutive(nums))
    
    
    
    
    
    
    
    
    
    
    
    