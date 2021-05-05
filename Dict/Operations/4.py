animal_list = ['kurka', 'Ryaba', 3, [1, 4], 'k']
animal_dict = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 3,
    'coords': [1, 4],
    'sprite': 'k'
}


# Удаление значения
animal_list.pop(-2)

animal_dict.pop('coords')

print(animal_dict)
