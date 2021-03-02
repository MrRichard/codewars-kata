# IQ Test kata - 03/01/2021
# https://www.codewars.com/kata/552c028c030765286c00007d

"""
Return the index of the number that differs from the others
"""
def iq_test(numbers):

    # Split and convert to ints
    numbers=[int(i) for i in numbers.split()]

    # Create lists of even and odd numbers
    evens=[]
    odds=[]
    for i in range(0,len(numbers)):
        evens.append(i) if numbers[i] % 2 == 0 else odds.append(i)

    # Return the set with fewer elements
    # Correct for index element offset of 1
    if len(odds) < len(evens):
        return odds[0]+1
    else:
        return evens[0]+1
    



# Run Tests
print(iq_test("2 4 7 8 10"))
print(iq_test("11 13 15 19 22"))
print(iq_test("2 2 4 6 8 9"))