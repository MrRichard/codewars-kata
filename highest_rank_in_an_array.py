#!/bin/env python

# Highest Rank Number in an Array
# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python 

# Problematic:  
# "If there is a tie for most frequent number, 
# return the largest number among them."

from collections import Counter

def highest_rank(arr):
    sort_arr = sorted(Counter(arr).items(), 
        reverse=True, 
        key=lambda x: (x[1],x[0]))

    return sort_arr[0][0]
    
# Test 
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10, 12]))