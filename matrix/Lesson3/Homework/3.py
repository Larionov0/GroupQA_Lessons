mat = [
    [4, 1, 3, 67, 0],
    [50, 23, 6, 4, 2],
    [8, 1, 4, 1, 1],
    [3, 0, 6, 33, 1]
]

i = 0
lst = []
while i < len(mat):
    j = 0
    sum = 0
    while j < len(mat[0]):
        sum += mat[i][j]
        j += 1
    i += 1
    lst.append(sum)
print("Сумма всех чисел в строке:", lst)

n = 0
max = 0
while n < len(lst):
    if lst[n] > max:
        max = lst[n]
    n += 1
print("Наибольшое значение:", max)

i = 0
for num in lst:
    if max == num:
        print("Номер ряда с наибольшим значением:", i + 1)
    i += 1
