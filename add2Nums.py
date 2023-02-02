#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:22:04 2023

@author: jamesboot
"""

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, 
# and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

def addTwoNumbers(l1, l2):
    
    l1.reverse()
    l2.reverse()
    
    s1 = [str(i) for i in l1]
    newnum1 = int("".join(s1))
    
    s2 = [str(i) for i in l2]
    newnum2 = int("".join(s2))
    
    sumnum = newnum1 + newnum2
    
    s3 = list(str(sumnum))
    
    s3.reverse()
    
    return s3

test1 = [2,4,3]
test2 = [5,6,4]
output1 = addTwoNumbers(test1, test2)

test3 = [9,9,9,9,9,9,9]
test4 = [9,9,9,9]
output2 = addTwoNumbers(test3, test4)

test5 = [0]
test6 = [0]
output3 = addTwoNumbers(test5, test6)
