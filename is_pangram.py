import string

# Codewars kata: Detect Pangram
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# 03/03/2021

def is_pangram(s):
    alpha='abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if s.lower().find(letter) < 0:
            return False
    return True

print(is_pangram('The quick, brown fox jumps over the lazy dog!'))