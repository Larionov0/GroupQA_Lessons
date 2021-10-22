names = ['Sasha', 'Alex', 'Bob', 'Vasya', 'Petya', 'Kirill']

r = list(filter(lambda name: 'a' in name.lower(), names))
print(r)
