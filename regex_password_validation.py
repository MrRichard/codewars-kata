#!/bin/env python3

# Solution for "Regex Password Validation"
# https://www.codewars.com/kata/52e1476c8147a7547a000811
# thank you https://regex101.com/

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number

regex="^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[a-zA-Z0-9]{6,}$"

# Test examples
import re

def test_password(password, regex):
    if re.match(regex, password):
        return True
    else:
        return False

test_passwords = ["FLAN001", "Flan001", "FLanflAN", "Fl1", "FLan0000" , "Flannery29" , "999FLANBoT" ]
for pw in test_passwords:
    print("Test password {}: {}".format(pw, test_password(pw, regex)))
