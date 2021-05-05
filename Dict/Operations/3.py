animal_list = ['kurka', 'Ryaba', 3, [1, 4], 'k']
animal_dict = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 3,
    'coords': [1, 4],
    'sprite': 'k'
}


# Добавить значение
animal_list.append(10)

animal_dict['satiety'] = 10

print(animal_dict)
