animal_list = ['kurka', 'Ryaba', 3, [1, 4], 'k']
animal_dict = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 3,
    'coords': [1, 4],
    'sprite': 'k'
}


# Замена значений
animal_list[1] = 'Masha'

animal_dict['name'] = 'Masha'

print(animal_dict)
