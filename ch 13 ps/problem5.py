# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

l = [2, 5, 7, 4, 0, 33, 9]

def greater(a,b):
    return a if a>b else b

print(f"The greatest number in the given list is {reduce(greater,l)}")