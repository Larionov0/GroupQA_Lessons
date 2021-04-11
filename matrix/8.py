"""
Вывести на экран сумму всех чисел матрицы
"""

matrix = [
    [1, 5, 3, 6],
    [7, 3, 6, 1],
    [4, 7, 8, 5]
]

sum_ = 0

i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[0]):
        sum_ += matrix[i][j]
        j += 1
    i += 1

print(sum_)
