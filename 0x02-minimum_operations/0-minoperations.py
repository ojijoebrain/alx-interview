#!/usr/bin/python3

"""
This script contains a function that calculates the fewest number of operations
needed to reach exactly `n` characters using Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations needed to obtain exactly `n`
    characters in the file.

    Parameters:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations, or 0 if `n` is less than or equal to 1.
    """
    if n <= 1:
        return 0

    now = 1
    start = 0
    counter = 0

    while now < n:
        remainder = n - now
        if remainder % now == 0:
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1

    return counter
