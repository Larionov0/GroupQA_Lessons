from Classes.game_object import GameObject
import random
from colors import *


class Rock(GameObject):
    def __init__(self, x, y, radius=6, color=BLACK):
        super().__init__(x, y, radius, color)

    def update(self, keys, game_objects):
        pass

    @classmethod
    def spawn_random(cls, global_width, global_height):
        rock = cls(
            x=random.randint(0, global_width),
            y=random.randint(0, global_height),
            radius=random.randint(5, 10)
        )
        return rock