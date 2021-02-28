#!/bin/env python

# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):
    # First Draft
    # results=[]
    # for ind in data:
    #     if ind[0] >= 55 and ind[1] > 7:
    #         results.append("Senior")
    #     else:
    #         results.append("Open")
    # return results

    # Second Draft
    return [ "Senior" if x[0] >= 55 and x[1] > 7 else "Open" for x in data ]

# Basic Test Case
results=open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]) # ['Open', 'Senior', 'Open', 'Senior']
print(results)
results=open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]) #['Open', 'Open', 'Senior', 'Open'])
print(results)