#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total >= coin:
            num_coins += total // coin
            total = total % coin

    if total != 0:
        return -1

    return num_coins
