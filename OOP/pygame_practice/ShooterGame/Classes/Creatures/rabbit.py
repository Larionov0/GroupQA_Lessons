from Classes.Creatures.enemy import *
from colors import *


class Rabbit(Enemy):
    def __init__(self, x, y, speed=2, radius=10, vision_radius=150, color=GREEN):
        super().__init__(x, y, speed, radius, vision_radius, color)

    def update(self, keys, game_objects):
        hero = self.find_nearby_enemy(game_objects)
        if hero:
            vector = [hero.x - self.x, hero.y - self.y]

            vector_size = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
            k = self.speed / vector_size if vector_size != 0 else 0
            normal_vector = [- vector[0] * k, - vector[1] * k]
            self.x += normal_vector[0]
            self.y += normal_vector[1]
        else:
            if time() - self.last_dir_choose_time > self.dir_vector_delay:
                self.choose_random_dir_vector()

            self.x += self.direction_vector[0]
            self.y += self.direction_vector[1]
