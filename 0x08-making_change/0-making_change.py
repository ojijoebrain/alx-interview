#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order to start with the largest denomination
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        # Use as many coins of this denomination as possible
        if total >= coin:
            num_coins += total // coin
            total = total % coin

    # If total is not 0, it means we cannot make the exact amount
    if total != 0:
        return -1

    return num_coins
