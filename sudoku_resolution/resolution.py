import numpy as np

"""
TO DO:
- create a list of values
- create a function check_column
- create a function check_row
- create a function check_square
"""

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
row = list(map(str, values))

grid_test = np.array([[None, None, None, None, 9, 2, None, None, 7],
                      [None, None, None, 6, None, None, None, None, None],
                      [2, 7, None, None, None, 1, None, 6, 8],
                      [6, None, None, None, None, None, None, 9, None],
                      [7, 9, None, 5, None, 3, None, 4, 6],
                      [None, 8, None, None, None, None, None, None, 2],
                      [5, 6, None, 3, None, None, None, 2, 9],
                      [None, None, None, None, None, 4, None, None, None],
                      [8, None, None, 1, 2, None, None, None, None]])


def parse_grid(grid):
    new_grid = {}
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            new_grid[columns[i] + row[j]] = grid[j, i]
    return new_grid


grid = parse_grid(grid_test)

def check_column(grid, col_index):
    possible_value = []
    return
