#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    grid: list of lists of integers where:
      - 0 represents water
      - 1 represents land
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four directions (up, down, left, right)
                if i == 0 or grid[i-1][j] == 0:  # up
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # right
                    perimeter += 1

    return perimeter
