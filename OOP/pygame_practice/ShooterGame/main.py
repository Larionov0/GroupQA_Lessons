import pygame
import random
from typing import Optional, Union
from time import sleep, time

from Classes.Creatures.bullet import Bullet
from Classes.Creatures.enemy import Enemy
from Classes.Creatures.rabbit import Rabbit
from Classes.Creatures.hero import Hero
from Classes.camera import Camera
from Classes.rock import Rock
from colors import *
from config import *


pygame.init()  # настройка пайгейма


def main():
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    hero = Hero('Bob', 300, 400, 5)
    game_objects = [
        hero,
        Enemy(100, 100),
        Enemy(700, 500),
        Enemy(500, 300),
        Enemy(200, 400),
        Rabbit(300, 400),
        Rabbit(240, 400),
    ]
    for _ in range(1000):
        game_objects.append(Rock.spawn_random(GLOBAL_WIDTH, GLOBAL_HEIGHT))

    camera = Camera(hero, WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                pass

            if event.type == pygame.KEYUP:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coords = event.pos  # [230, 154]

                hero.shoot(mouse_coords[0], mouse_coords[1], game_objects, camera)

        keys = pygame.key.get_pressed()

        screen.fill(WHITE)

        for game_object in game_objects:
            if game_object.is_alive:
                game_object.update(keys, game_objects)
        Enemy.check_is_it_time_to_spawn(game_objects)

        for game_object in game_objects:
            if game_object.is_alive:
                game_object.draw(screen, camera)

        game_objects = [game_object for game_object in game_objects if game_object.is_alive]  # game_objects = list(filter(lambda game_object: game_object.is_alive), game_objects)

        pygame.display.flip()
        clock.tick(FPS)


main()
