import pickle


weapon = {
    'name': 'меч Силы',
    'damage': 5,
    'dur': 10
}

castle = {
    'name': 'Замок крови',
    'square': 1000
}

heroes = [
    {
        'name': 'Alan',
        'hp': 10,
        'castle': castle
    },
    {
        'name': 'Petro',
        'hp': 5,
        'castle': castle
    }
]


print(heroes[0]['castle'] is heroes[1]['castle'])

with open('heroes.dat', 'wb') as file:
    pickle.dump(heroes, file)


with open('heroes.dat', 'rb') as file:
    heroes2 = pickle.load(file)

print(heroes2[0]['castle'] is heroes2[1]['castle'])
