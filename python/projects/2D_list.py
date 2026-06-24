numbers_grid = [
    [3, 5, 2],
    [7, 1, 9],
    [4, 6, 8]
]

for i in range(len(numbers_grid)):
    for c in range(len(numbers_grid[i])):
        numbers_grid[i][c] = numbers_grid[i][c] * 2
print(numbers_grid)

