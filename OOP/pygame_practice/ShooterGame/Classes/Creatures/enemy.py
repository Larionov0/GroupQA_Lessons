from Classes.Creatures.creature import Creature
import pygame
from time import time
from typing import Optional
from colors import *
from config import *
import random
from help_functions import *


class Enemy(Creature):
    side = 'ополчение'
    last_spawn_time = time()

    def __init__(self, x, y, speed=2, radius=10, vision_radius=150, color=RED):
        super().__init__(x, y, speed, radius, color)
        self.direction_vector = [0, 0]
        self.last_dir_choose_time = time()
        self.dir_vector_delay = random.randint(16, 24) / 10
        self.vision_radius = vision_radius

    def find_nearby_enemy(self, game_objects) -> Optional['Hero']:
        for obj in game_objects:
            if isinstance(obj, Creature):
                if obj.side in ('альянс', "культ ведьмы"):
                    if distance([self.x, self.y], [obj.x, obj.y]) < self.vision_radius:
                        return obj

    def update(self, keys, game_objects):
        hero = self.find_nearby_enemy(game_objects)
        if hero:
            vector = [hero.x - self.x, hero.y - self.y]

            vector_size = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
            k = self.speed / vector_size if vector_size != 0 else 0
            normal_vector = [vector[0] * k, vector[1] * k]
            self.x += normal_vector[0]
            self.y += normal_vector[1]
        else:
            if time() - self.last_dir_choose_time > self.dir_vector_delay:
                self.choose_random_dir_vector()

            self.x += self.direction_vector[0]
            self.y += self.direction_vector[1]

    def choose_random_dir_vector(self):
        x_dir = random.randint(-10, 10) / 10
        y_dir = random.randint(-10, 10) / 10

        vector_size = (x_dir ** 2 + y_dir ** 2) ** 0.5
        k = self.speed / 2 / vector_size if vector_size != 0 else 0
        normal_vector = [x_dir * k, y_dir * k]
        self.direction_vector = normal_vector
        self.last_dir_choose_time = time()
        return normal_vector

    @classmethod
    def spawn_random(cls, global_width=GLOBAL_WIDTH, global_height=GLOBAL_HEIGHT):
        return cls(
            x=random.randint(0, global_width),
            y=random.randint(0, global_height),
            speed=random.randint(20, 40) / 10,
            radius=random.randint(8, 12),
            color=(random.randint(200, 255), random.randint(0, 50), random.randint(0, 50)),
            vision_radius=random.randint(130, 200)
        )

    @classmethod
    def check_is_it_time_to_spawn(cls, game_objects):
        cur_time = time()

        if cur_time - cls.last_spawn_time > 4:  # раз в 4 секунды спавним врага
            game_objects.append(cls.spawn_random())
            cls.last_spawn_time = cur_time

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.global_to_local_coords(self.x, self.y), self.radius)
        pygame.draw.circle(screen, BLACK, camera.global_to_local_coords(self.x, self.y), self.vision_radius, width=1)
