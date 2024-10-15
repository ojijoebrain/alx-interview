#!/usr/bin/python3
"""
Prime Game
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determines the winner after x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_set = [i for i in range(1, n + 1) if is_prime(i)]
        maria_turn = True

        while prime_set:
            prime = prime_set[0]
            prime_set = [i for i in prime_set if i % prime != 0]

            if maria_turn:
                maria_turn = False
            else:
                maria_turn = True

        if not maria_turn:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
