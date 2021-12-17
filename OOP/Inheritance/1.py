class Human:
    def __init__(self, name, age=0, money=0, sex='m'):
        self.name = name
        self.age = age
        self.money = money
        self.sex = sex

    def say_hi(self):
        print(f"{self.name}: 'Hello'")

    def say_hi_to_smwn(self, other):
        print(f"{self.name}: 'Hello, {other.name}'")

    def grow(self):
        self.age += 1
        print(f'{self.name} подрос на год. Теперь ему/ей {self.age} лет.')

    def __str__(self):
        return f"Human {self.name} (age:{self.age}; money:{self.money})"


class Worker(Human):
    def __init__(self, name, age=18, money=0, sex='m', job='', salary=1000):
        super().__init__(name, age, money, sex)

        self.job = job
        self.salary = salary

    def work(self):
        if self.job == 'токарь':
            print(f'{self.name}: * звуки точения *')
        elif self.job == 'программист':
            print(f'{self.name}: * звуки клавиатуры *')
        elif self.job == 'менеджер':
            print(f'{self.name}: * звуки разговоров *')

        self.money += self.salary
        print(f"{self.name} получил зп = {self.salary}. Теперь у него {self.money} денег")

    def say_hi(self):
        print(f"{self.name}: 'Ну здарова'")

    def grow(self):
        super().grow()
        self.money += self.salary // 2
        print(f"{self.name} получил подарок {self.salary // 2}. Теперь у него {self.money}")


h1 = Human('Bob', 20, 1000)
h2 = Human('Alex', 15, 200)

w1 = Worker('Petya', 20, 10000, job='менеджер')

h1.grow()
w1.grow()
