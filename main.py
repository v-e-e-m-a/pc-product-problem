def max_list(list):
    max = list[0]
    for i in range(len(list) - n):
        product = list[i]
        for j in range(i+1, n + i):
            product *= list[j]
        if product > max:
            max = product
    return max

def largest_product(grid, n):
    max = grid[0][0]
    flat_horizontal = []
    flat_vertical = []

    num_row = len(grid)
    num_col = len(grid[0])

    for i in range(num_row): # Number of rows in the grid
        for j in range(num_col): # Number of elements in the row
            flat_horizontal.append(grid[i][j])
            flat_vertical.append(grid[j][i])

    max_horizontal = max_list(flat_horizontal)
    max_vertical = max_list(flat_vertical)

    if max_horizontal > max_vertical:
        return max_horizontal
    else:
        return max_vertical
    
    # Start at the beginning of list
    # Nested for loop starting at second element
    # Iterate the nested loop for n - 2 times
'''    
    for i in range(len(flat_horizontal)):
        product = flat_horizontal[i]
        for j in range(i+1, n + i):
            product *= flat_horizontal[j]
        if product > max:
            max = product
'''



grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
expected = 670824  # 99 * 88 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12]
]
n = 2
expected = 7623  # 99 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2, 3],
    [4, 5, 6]
]
n = 3
expected = 120  # 4 * 5 * 6
assert largest_product(grid, n) == expected

grid = [
    [-1],
    [2],
    [-3]
]
n = 2
expected = -2  # -1 * 2
assert largest_product(grid, n) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
