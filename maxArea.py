#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:28:33 2023

@author: jamesboot
"""

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Double for loop to iterate through

def maxArea(heights):

    areaList = []

    for pos1 in range(len(heights)):
        
        X1 = pos1+1
        Y1 = heights[pos1]
        
        for pos2 in range(len(heights)):
            
            X2 = pos2+1
            Y2 = heights[pos2]
            
            area = (X2-X1)*min(Y1, Y2)
            
            areaList.append(area)
            
    return max(areaList)

height = [1,8,6,2,5,4,8,3,7]

height = [1,1]

height = [4,6,2,6,8,4,3,1,5,7,8,5,2,1,5,7,4,2,6,7,8,89,8,8,9,3,2,4,6,8,4]

print(maxArea(height))


