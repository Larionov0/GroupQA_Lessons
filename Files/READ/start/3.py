file = open('Files/test1.txt', 'rt')

lines = file.readlines()  # возвращает список всех линий в файле
print(lines[2])

file.close()
