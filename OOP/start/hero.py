class Hero:
    name = ''
    age = 0
    money = 0
    is_male = True

    damage = 3
    hp = max_hp = 15
    armor = 1
    is_alive = True

    weapon = None

    def say_hi(self):
        print(f'{self.name}: Hello')

    def say_hi_to_someone(self, hero):
        print(f'{self.name}: "Hello, {hero.name}"')

    def grow_up(self):
        self.age += 1
        if self.is_male:
            print(f'Герой {self.name} подрос на год. Теперь ему {self.age} лет.')
        else:
            print(f'Героиня {self.name} подросла на год. Теперь ей {self.age} лет.')

    def attack(self, enemy):
        print(f'{self.name} наносит удар по {enemy.name}')
        damage = self.damage
        if self.weapon and self.weapon.is_alive:
            damage += self.weapon.plus_attack()
        enemy.get_damage(damage)

    def get_damage(self, damage):
        remaining_damage = damage - self.armor
        print(f'В {self.name} прошло {remaining_damage}/{damage} урона.')
        if remaining_damage > 0:
            self.loose_hp(remaining_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        print(f'У {self.name} остается {self.hp}/{self.max_hp} hp')
        if self.hp <= 0:
            self.die()

    def die(self):
        print(f'Герой {self.name} откинул копыта')
        self.is_alive = False


class Weapon:
    name = ''
    type = ''
    sound = ''
    damage = 1
    durability = 4
    is_alive = True

    def plus_attack(self) -> int:
        self.durability -= 1
        print(f'{self.name}: {self.sound}. Осталось {self.durability} прочности. Добавлено {self.damage} урона')
        if self.durability <= 0:
            self.break_()
        return self.damage

    def break_(self):
        self.is_alive = False
        print(f'Оружие {self.name} сломалось')


def battle(hero1: Hero, hero2: Hero):  # ни на что не влияет, подсказка прогеру
    round_ = 1
    while hero1.is_alive and hero2.is_alive:
        print(f'\n\n-----= Round {round_} =-----')
        hero1.attack(hero2)
        print('\n\n')
        hero2.attack(hero1)
        round_ += 1

    if hero1.is_alive:
        print(f'Победитель - {hero1.name}')
    elif hero2.is_alive:
        print(f'Победитель - {hero2.name}')
    else:
        print('Все откинулись. Ничья')


h1 = Hero()
h1.name = 'Bob'
h1.age = 20

h1.hp = h1.max_hp = 25
h1.damage = 2
h1.armor = 2

h2 = Hero()
h2.name = 'Vasya'

h2.armor = 1
h2.hp = h2.max_hp = 15
h2.damage = 4

h3 = Hero()
h3.name = 'Evelyn'
h3.age = 26
h3.is_male = False


sword = Weapon()
sword.name = 'Меч огня'
sword.sound = 'Вжик'
sword.durability = 2
sword.damage = 3
sword.type = 'sword'

dubina = Weapon()
dubina.name = 'Изогнутая дубина'
dubina.sound = 'Бах'
dubina.damage = 1
dubina.durability = 20
dubina.type = 'stick'

h1.weapon = dubina
h2.weapon = sword

battle(h1, h2)

