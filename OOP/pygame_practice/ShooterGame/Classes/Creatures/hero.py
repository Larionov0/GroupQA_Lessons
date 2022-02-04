from Classes.Creatures.creature import Creature
from Classes.Creatures.bullet import Bullet
from Classes.Creatures.enemy import Enemy
from colors import *
import pygame


class Hero(Creature):
    is_hero = True
    side = 'альянс'

    def __init__(self, name, x, y, speed=5, radius=20, color=BLUE):
        super().__init__(x, y, speed, radius, color)
        self.name = name

    def update(self, keys, game_objects):
        """
        Метод, который будет вызываться на каждой итерации основного цикла программы
        """
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def shoot(self, mouse_x, mouse_y, game_objects, camera):
        # пересчитываем координаты героя из глобальных в локальные, чтобы правильно построить вектор направления пули
        local_x, local_y = camera.global_to_local_coords(self.x, self.y)
        vector = [mouse_x - local_x, mouse_y - local_y]
        vector_size = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        k = 10 / vector_size if vector_size != 0 else 0
        normal_vector = [vector[0] * k, vector[1] * k]
        bullet = Bullet(self.x, self.y, normal_vector, target_type=Enemy)
        game_objects.append(bullet)
