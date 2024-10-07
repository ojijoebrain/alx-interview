# Island Perimeter

## Description

This project involves calculating the perimeter of an island in a rectangular grid. The island is represented by `1`s (land) and is surrounded by water, which is represented by `0`s. Each cell is a square with a side length of 1. The island has no lakes, and the grid is completely surrounded by water. There is only one island.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- Your code must follow the PEP 8 style (version 1.7).
- No modules or libraries are imported.
- The code should be executable.

## Prototype

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    grid: list of list of integers where:
      - 0 represents water
      - 1 represents land
    """
