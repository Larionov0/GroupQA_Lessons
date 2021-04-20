matrix = [
    [4, 1, 3, 67, 0, 3, 2],
    [50, 23, 6, 4, 2, 6, 3],
    [88, 89, 4, 1, 1, 8, 4],
    [3, 0, 6, 33, 44, 1, 7]
]


i = int(input())

j = 0
while j < len(matrix[0]):
    matrix[i][j] = 0
    j += 1

print(matrix)
