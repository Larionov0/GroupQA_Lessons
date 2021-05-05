animal_list = ['kurka', 'Ryaba', 3, [1, 4], 'k']
animal_dict = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 3,
    'coords': [1, 4],
    'sprite': 'k'
}

# Перебор элементов

# for el in animal_list:
#     print(el)

for key, value in animal_dict.items():
    print(key, ':', value)
