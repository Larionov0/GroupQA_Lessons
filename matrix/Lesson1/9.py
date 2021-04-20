"""
Вывести на экран столбец с максимальной
суммой элементов.
"""

matrix = [
    [1, 5, 3, 6],
    [7, 3, 6, 1],
    [4, 7, 8, 5]
]

max_j = None
max_sum = 0

j = 0
while j < len(matrix[0]):  # j = 1
    sum_ = 0
    for row in matrix:
        number = row[j]
        sum_ += number

    if sum_ > max_sum:
        max_sum = sum_
        max_j = j
    j += 1


for row in matrix:
    print(row[max_j])
