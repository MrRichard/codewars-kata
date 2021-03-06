#!/bin/env python

# Make a function that does arithmetic
# https://www.codewars.com/kata/583f158ea20cfcbeb400000a
# This day in history: Day after my second covid shot. My brain is no worky.

def arithmetic(a, b, operator):
    # Dictionary of viable inputs
    operators = {
        "add" : "+",
        "subtract": "-",
        "divide" : "/",
        "multiply" : "*"
    }

    # Validate input since we are using eval
    if operator in operators and isinstance(a,int) and isinstance(b,int):
        return eval(str(a) + operators[operator] + str(b))
    return False

print(arithmetic(4,5,'multiply'))
print(arithmetic(100,25,'subtract'))
print(arithmetic(11,25,'add'))
print(arithmetic(12,3,'divide'))
print(arithmetic(11,25,'mod'))

""" 
After submitting my example and seeing other's submissions: 
I probably overthought this problem by:
a) Using a dictionary of options 
b) Evaluting the equation as a string
c) Worrying about security because of using eval() and thusly
wanting to validating all input. 

In hindsight, I would probably create a simple series of if / elif 
logic that returns "a/b" or "a*b" depending on the operator.
"""