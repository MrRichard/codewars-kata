#!/bin/env python

# https://www.codewars.com/kata/556deca17c58da83c00002db/
# "This was a lot simplier after I figured it out."

def tribonacci(signature, n):
    if n == 0: 
        return []

    for _ in range(3,n): # offset for the original 3
        signature.append(sum(signature[-3:]))
    return signature[:n]

print(tribonacci([1, 1, 1], 10))
print(tribonacci([126, 68, 53], 2))
# expected output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]