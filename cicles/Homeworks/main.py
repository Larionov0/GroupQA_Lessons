names = ['Bob', 'Katia', 'Lera', 'Vasya']
marks = [12, 4, 7, 5]

ogr = len(marks) - 1
while ogr != 0:
    i = 0
    while i < ogr:
        if marks[i] > marks[i + 1]:
            marks[i], marks[i + 1] = marks[i + 1], marks[i]
            names[i], names[i + 1] = names[i + 1], names[i] 
        i += 1
    ogr -= 1

print(names)
print(marks)
