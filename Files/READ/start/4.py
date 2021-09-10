file = open('Files/test1.txt', 'rt')

for line in file:  # перебор строк файла
    print('---' + line)

file.close()
