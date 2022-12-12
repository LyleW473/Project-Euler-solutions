def find_lattice_paths(n):

    # Create a grid with n +  1 columns, n + 1rows. (0, 0) will be the starting point 
    # This is because for a 2 x 2 grid, the starting point would need to be (0, 0), the ending point would be (2, 2)
    my_grid = [[1 for y in range(n + 1)] for x in range(n + 1)]

    # For each row in range(0, n + 1)
    for row in range(1, n + 1): 
        # For each column in range(0, n + 1)
        for column in range(1, n + 1):

            # Set the current item to be the sum of: The item to the left of the current item and the item above the current item
            # Note@ This sets the current item to be the amount of 
            my_grid[row][column] = my_grid[row - 1][column] + my_grid[row][column-1]

    # Return the bottom-right item (the last item in the grid)
    return my_grid[n][n]

print(find_lattice_paths(20))