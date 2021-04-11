"""
Вывести на экран сумму всех чисел матрицы
"""

matrix = [
    [1, 5, 3, 6],
    [7, 3, 6, 1],
    [4, 7, 8, 5]
]

sum_ = 0
for row in matrix:
    for number in row:
        sum_ += number
print(sum_)
