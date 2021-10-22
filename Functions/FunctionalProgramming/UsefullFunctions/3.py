names = ['Bob', 'Alex', 'Petya', 'Vasya']
marks = [12, 4, 10, 9]
sexs = ['m', 'f', 'm', 'm']


for name, mark, sex in zip(names, marks, sexs):
    print(name, mark, sex)
