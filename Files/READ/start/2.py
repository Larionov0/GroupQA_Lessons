file = open('Files/test1.txt', 'rt')

line1 = file.readline()  # считывает одну строку (вместе с переносом \n)
print(line1)

line2 = file.readline()
print(line2)

text = file.read(2)
print(text)

file.close()
