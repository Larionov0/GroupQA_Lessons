names = ['Bob', 'Alex', 'Petya', 'Vasya']


for i, name in enumerate(names):
    if 'a' in name.lower():
        names[i] += '!'

print(names)
