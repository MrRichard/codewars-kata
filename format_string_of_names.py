#!/bin/env python

# https://www.codewars.com/kata/53368a47e38700bd8300030d
# 03/20/2021

# If no names, return []
# If one name return name
# If using two names use &
# If +2 names, use comma listing and &

def namelist(names):
    number=len(names)
    if number == 0:
        return ''
    elif number == 1:
        return names[0]['name']
    elif number == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    else:
        # join + list comprehension + array slicing + dict index name = ugly code
        return  ", ".join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]["name"]

# Test the results
a=namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
#a=namelist([{'name': 'Bart'},{'name': 'Lisa'}])
#a=namelist([])
print(a)
