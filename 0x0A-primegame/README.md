# Prime Game

## Description

The **Prime Game** is a two-player game where Maria and Ben take turns choosing a prime number from a set of consecutive integers. Each player removes the chosen prime number and all its multiples from the set. The game continues until no more moves are possible, and the player who cannot make a move loses.

In this project, we implemented the function `isWinner(x, nums)` to determine who wins the most rounds in multiple game sessions.

- Maria always plays first.
- Both Maria and Ben play optimally.
- The game ends when no prime numbers are available to choose.

## Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.
    Args:
    - x (int): the number of rounds to be played.
    - nums (list): list of integers, where each integer represents the highest number (n) for the round.

    Returns:
    - str: The name of the player who won the most rounds. ("Maria" or "Ben")
    - None: If the winner cannot be determined (if both win the same number of rounds).
    """
