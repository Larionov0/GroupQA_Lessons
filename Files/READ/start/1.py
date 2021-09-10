file = open('Files/test1.txt', 'rt')

text1 = file.read(5)  # читает 5 символов с файла
# print(text1)

text2 = file.read(3)
# print(text2)

text3 = file.read()  # читает весь оставшийся файл
# print(text3)

text4 = file.read()
print(repr(text4))

file.close()
