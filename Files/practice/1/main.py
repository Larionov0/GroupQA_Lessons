def file_increaser(filename1, filename2, number=1):
    """
    Считывает числа из первого файла, добавляет к каждому числу файла number
    Затем записівает числа в том же порядке во второй файл
    """
    numbers_matrix = []

    file = open(filename1, 'rt', encoding='utf-8')
    for line in file:  # '3 2 53 45 64 234 45 23\n'
        numbers_str = line.rstrip().split(' ')  # ['3', '2', '53', '45', '64', ...]
        numbers_matrix.append(
            [str(int(numb_str) + number) for numb_str in numbers_str]
        )
    file.close()

    file2 = open(filename2, 'wt', encoding='utf-8')
    for row in numbers_matrix:  # ['4', '3', '54', '46', '65', '235', '46', '24']
        file2.write(' '.join(row) + '\n')
    file2.close()


# file_increaser('FILES/test_file.txt', 'FILES/result_file.txt', 1)

file_increaser('FILES/test_file2.txt', 'FILES/result_file2.txt', 50)
