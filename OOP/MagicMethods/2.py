class Hero:
    def __init__(self, name, hp=20, attack=3):
        print(f'Был создан {name}')
        self.name = '<' + name + '>'
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def __str__(self):  # str
        return f"Герой {self.name} (hp={self.hp}/{self.max_hp}; attack={self.attack})"


h1 = Hero('Bob', 10, 2)
h2 = Hero('Petya')

print(h1)
print(h2)

