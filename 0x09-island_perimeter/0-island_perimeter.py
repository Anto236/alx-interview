#!/usr/bin/python3

"""
This module defines the function `island_perimeter` to
calculate the perimeter of an island described in a grid.

Grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
Grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that
isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A list of lists representing the grid.

    Returns:
        int: The calculated perimeter of the island.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                """Start with assuming all sides are contributing"""

                """Check left neighbor"""
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                """Check upper neighbor"""
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
