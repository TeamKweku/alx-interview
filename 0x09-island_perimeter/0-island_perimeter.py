#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Compute the perimeter of an island represented by a grid.

    Args:
        grid (list): A list of lists representing the grid where 1s represent
                     land and 0s represent water.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
