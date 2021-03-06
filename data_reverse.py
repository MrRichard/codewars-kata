#!/bin/env python

# Traning on Data Reverse
# https://www.codewars.com/kata/569d488d61b812a0f7000015

# After writing far too much code for this problem, I shamelessly copied a similar example from:
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
# I used slicing [::-1] to reverse the groups (which I thought was slick), and then 
# created a new list from the various sublists

def data_reverse(data):
    reversed_groups = [data[i * 8:(i + 1) * 8] for i in range((len(data) + 8 - 1) // 8 )][::-1]
    return [j for i in reversed_groups for j in i]

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))