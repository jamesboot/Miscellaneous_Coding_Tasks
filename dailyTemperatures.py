#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:19:46 2023

@author: jamesboot
"""

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days 
# you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    
    output = []
    
    for x in range(len(temperatures)):
        
        temp1 = temperatures[x]
        
        counts = 0
        
        if x == len(temperatures)-1:
            
            counts = 0
            output.append(counts)
            break
        
        newlist = temperatures[x+1:len(temperatures)]
        
        if all(i < temp1 for i in newlist):
            
            counts = 0
            output.append(counts)
            continue
        
        for y in range(x+1,len(temperatures)):
            
            temp2 = temperatures[y]
            
            if temp1 < temp2:
                
                counts += 1
                output.append(counts)
                break
            
            elif temp1 > temp2:
                
                counts += 1
    
    return output

test1 = [73,74,75,71,69,72,76,73]
test2 = [30,40,50,60]
test3 = [30,60,90]

print(dailyTemperatures(test1))
print(dailyTemperatures(test2))
print(dailyTemperatures(test3))



