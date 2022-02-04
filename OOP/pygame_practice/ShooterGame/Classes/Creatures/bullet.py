from Classes.Creatures.creature import Creature
from colors import *
from help_functions import *


class Bullet(Creature):
    def __init__(self, x, y, dir_vector, speed=10, radius=3, color=BLACK, target_type: type = None):
        super().__init__(x, y, speed, radius, color)
        self.dir_vector = dir_vector
        self.target_type = target_type

    def update(self, keys, game_objects):
        self.x += self.dir_vector[0]
        self.y += self.dir_vector[1]

        for game_object in game_objects:
            if isinstance(game_object, self.target_type):
                if distance([self.x, self.y], [game_object.x, game_object.y]) < self.radius + game_object.radius:
                    game_object.die()
                    self.die()
                    break
