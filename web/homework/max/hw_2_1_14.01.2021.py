from typing import List, Tuple, Optional


class Location:
    def __init__(self, room: str):
        self.room = room
        self._connection = []

    def add_connection(self, conn):
        self._connection.append(conn)

    def get_connection(self):
        return self._connection

    def get_distance_to(self, loc2):
        return [con for con in self._connection if loc2 in [con.l1, con.l2]][0].d

    def __str__(self):
        return f"{self.room} ({len(self._connection)})"

    def __repr__(self):
        return self.__str__()


class Connection:
    def __init__(self, location_1, location_2, distance):
        self.l1: Location = location_1
        self.l2: Location = location_2
        self.d = distance
        self.l1.add_connection(self)
        self.l2.add_connection(self)


class uList(list):
    def __setitem__(self, key, value):
        raise uListError


class Hero:
    def __init__(self, location):
        self.location: Location = location
        self._passed_location = [location]
        self.passed_distance = 0

    @property
    def passed_location(self):
        return self._passed_location.copy()

    def go_to_location(self, loc: Location):
        self.passed_distance += self.location.get_distance_to(loc)
        self._passed_location.append(loc)
        self.location = loc


a = Location('кухня')
b = Location('спальня')
c = Location('гараж')


con1 = Connection(a, b, 15)
con2 = Connection(b, c, 10)
# print(con1.__dict__)
# print(con2.__dict__)


hero = Hero(a)
hero.go_to_location(b)
hero.go_to_location(c)

print(hero.passed_location)
print(hero.passed_distance)
