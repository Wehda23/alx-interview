#!/usr/bin/python3
"""
Island Permiter
"""


def island_perimeter(grid) -> int:
    """
    This function calculates the perimeter of an island in a given grid.
    """
    perimeter: int = 0
    rows: int = len(grid)
    cols: int = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check the cell above (if not in the first row)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check the cell to the left (if not in the first column)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
