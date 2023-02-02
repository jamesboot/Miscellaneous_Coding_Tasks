#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:39:43 2023

@author: jamesboot
"""

# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    
    # Make an empty set to put things in
    char_set = set()
    count = 0
    position = 0
    lengths = []
    
    while position < len(s):
        if s[position] not in char_set:
            char_set.add(s[position])
            count += 1
            position += 1
        else:
            lengths.append(count)
            char_set = set()
            char_set.add(s[position])
            count = 1
            position += 1
            
    return max(lengths)

s = 'pwwkew'

lengthOfLongestSubstring(s)
