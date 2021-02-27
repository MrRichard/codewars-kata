#!/bin/env python3

# simple letter substitution cipher that replaces a letter 
# with the letter 13 afer it in the alphabet.

import sys

# The function for the kata
def rot13(message):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            if (char.isupper()):
                result+=chr((ord(char) + 13 - 65) % 26 + 65)
            else:
                result+=chr((ord(char) + 13 - 97) % 26 + 97)
        else:
            result+=char
    return result

print(rot13(sys.argv[1]))