#!/usr/bin/python3

"""
   The method to determines the num of minmum operations for given n char
"""

def minOperations(n):
    """ A function that calculates the fewest number of operations """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
