class Human:
    def __init__(self, name, age, sex, skills, hp):
        self.__name = name
        self._age = age
        self.sex = sex
        self.skills = skills
        self._hp = hp
        self._is_alive = True

    @property
    def hp(self):
        return self._hp

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self._age

    def loose_hp(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self.die()

    # @age.setter  # в этом сеттере нету смысла, но для примера хорош
    # def age(self, new_age):
    #     if new_age != self._age + 1:
    #         raise ValueError(f'Возраст перескочил с {self._age} к {new_age}')
    #     self._age = new_age

    def die(self):
        print(f'{self.name} погиб')
        self._is_alive = False

    def grow_up(self):
        self._age += 1

    def say_something(self, smth):
        print(f"{self._name}: {smth}")

    def __str__(self):
        return f"{self.name} (age={self.age}; {self.sex}; hp={self.hp})"


class Worker(Human):
    def work(self):
        print(f"{self.name} working...")


human = Worker('Kirill', 25, 'm', ['пиано', "бокс", "экономика"], 10)
human.loose_hp(15)
print(human.hp)
