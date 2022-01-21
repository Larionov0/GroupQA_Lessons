import pygame
import random
from typing import Optional, Union
from time import sleep, time
pygame.init()  # настройка пайгейма

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1300
HEIGHT = 750
GLOBAL_WIDTH = 10000
GLOBAL_HEIGHT = 10000

FPS = 60


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


class GameObject:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.is_alive = True

    def update(self, keys, game_objects):
        raise NotImplementedError

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.global_to_local_coords(self.x, self.y), self.radius)

    def die(self):
        self.is_alive = False


class Creature(GameObject):
    def __init__(self, x, y, speed: float, radius, color):
        super().__init__(x, y, radius, color)
        self.speed = speed


class Hero(Creature):
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
        bullet = Bullet(self.x, self.y, normal_vector)
        game_objects.append(bullet)


class Enemy(Creature):
    last_spawn_time = time()

    def __init__(self, x, y, speed=2, radius=10, vision_radius=150, color=RED):
        super().__init__(x, y, speed, radius, color)
        self.direction_vector = [0, 0]
        self.last_dir_choose_time = time()
        self.dir_vector_delay = random.randint(16, 24) / 10
        self.vision_radius = vision_radius

    def find_hero(self, game_objects) -> Optional[Hero]:
        for obj in game_objects:
            if isinstance(obj, Hero):
                if distance([self.x, self.y], [obj.x, obj.y]) < self.vision_radius:
                    return obj

    def update(self, keys, game_objects):
        hero = self.find_hero(game_objects)
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


class Bullet(Creature):
    def __init__(self, x, y, dir_vector, speed=10, radius=3, color=BLACK):
        super().__init__(x, y, speed, radius, color)
        self.dir_vector = dir_vector

    def update(self, keys, game_objects):
        self.x += self.dir_vector[0]
        self.y += self.dir_vector[1]

        for game_object in game_objects:
            if isinstance(game_object, Enemy):
                if distance([self.x, self.y], [game_object.x, game_object.y]) < self.radius + game_object.radius:
                    game_object.die()
                    self.die()
                    break


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


class Camera:
    def __init__(self, hero, width, height):
        self.hero = hero
        self.width = width
        self.height = height

    def global_to_local_coords(self, global_x, global_y):
        x_left_up = self.hero.x - self.width // 2
        y_left_up = self.hero.y - self.height // 2

        local_x = global_x - x_left_up
        local_y = global_y - y_left_up

        return [local_x, local_y]


def main():
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    hero = Hero('Bob', 300, 400, 5)
    game_objects = [
        hero,
        Enemy(100, 100),
        Enemy(700, 500),
        Enemy(500, 300),
        Enemy(200, 400),
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
