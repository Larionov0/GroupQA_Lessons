students = [{'name': 'Petya', 'mark': 90}, {'name': 'Mark', 'mark': 67}]

if all([student['mark'] >= 90 for student in students]):
    print('Все отличники')
else:
    print('Нет')


if any([60 <= student['mark'] < 75 for student in students]):
    print('Есть двоечники')
else:
    print('Нету двоечников')
