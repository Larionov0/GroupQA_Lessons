"""Задание 2: Граф локаций
Задача:
Нужно написать приложение, работающее с локациями,
Для него понадобится реализовать следующий функционал:

Нужно реализовать возможность создавать локации с названиями, соединять их линиями соединения,
и задавать расстояние между соответствующими локациями. Как показано на картинке ниже.

Затем нужно прописать Героя, и интерфейс для того, чтоб пользователь мог перемещаться с локации на соседние локации.
При этом должно считаться суммарное расстояние, преодоленное героем. И в любой момент пользователь может нажать
на кнопочку, и ему выведется на экран это расстояние.

Создай классы:
- Location
- Connection
- Hero

Создание и соединение локаций должно быть в таком формате:
l1 = Location('спальня')
l2 = Location('туалет')

c = Connection(l1, l2, 6)

А еще лучше упаковать это в метод локации
l1 = Location('спальня')
l2 = Location('туалет')
l1.connect(l2, 6)"""


class Location:
    # map = {}

    def __init__(self, room: str):
        self.room = room
        self._connections = []

    def add_connection(self, conn):
        self._connections.append(conn)


class Connection:
    map = []

    def __init__(self, location_1, location_2, distance):
        self.l1: Location = location_1
        self.l2: Location = location_2
        self.d = distance
        # Connection.add_map(self.l1.room, self.l2.room, self.d)

        self.l1.add_connection(self)
        self.l2.add_connection(self)

    def __str__(self):
        return str(self.map)

    @classmethod
    def add_map(cls, loc1, loc2, dist):
        if loc1 not in cls.map:
            cls.map[loc1] = {loc2: dist}
        cls.map[loc1][loc2] = dist
        if loc2 not in cls.map:
            cls.map[loc2] = {loc1: dist}
        cls.map[loc2][loc1] = dist


class Hero:
    def __init__(self):
        self.distance = 0
        self.passed_locations = []
        self.map = Connection.map

    def get_distance(self):
        print(f"LOCATION: {self.map}")
        way = ''
        try:
            for i in range(len(self.passed_locations) - 1):
                way = f'{self.passed_locations[i].room}'
                d = self.map[self.passed_locations[i].room][self.passed_locations[i + 1].room]
                if d:
                    self.distance += d
        except KeyError:
            print(f"прошел до {way.upper()}, дальше нет пути!")
        finally:
            return f"Итого прошел: {self.distance}"

    def go_to_location(self, loc):
        pass


a = Location('кухня')
b = Location('спальня')
c = Location('гараж')

d1 = Connection(a, b, 10)
d2 = Connection(a, c, 50)
d3 = Connection(b, c, 15)

hero = Hero(a, b, c, a, a)
print(hero.get_distance())











