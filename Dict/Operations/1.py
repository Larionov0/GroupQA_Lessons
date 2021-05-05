animal_list = ['kurka', 'Ryaba', 3, [1, 4], 'k']
animal_dict = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 3,
    'coords': [1, 4],
    'sprite': 'k',
    100: True  # безсмыслица, просто для примера
}


# Достать значение
print(animal_list[2])

print(animal_dict['hp'])
print(animal_dict[100])
