#!/usr/bin/python3
# Iterate through the list:
def island_perimeter(grid):
    """
    This function calculates the perimeter of a grid by
    taking the calculation of sides
    Parameter:
        grid: A 2D matrix that represents the area covered by land an water
    """
    perimeter = 0
    # Loop through row indices
    for row in range(len(grid)):
        # Loop through column indices
        for col in range(len(grid[row])):
            # Check if the cell is land (1)
            if grid[row][col] == 1:
                # Check the left side
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check the right side
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                # Check the top side
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check the bottom side
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return(perimeter)
