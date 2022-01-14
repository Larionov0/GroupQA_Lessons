import pygame
import random
from time import sleep, time
pygame.init()  # настройка пайгейма

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1000
HEIGHT = 600

FPS = 60


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


class Creature:
    def __init__(self, x, y, speed, radius, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color
        self.is_alive = True

    def update(self, keys, creatures):
        raise NotImplementedError

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def die(self):
        self.is_alive = False


class Hero(Creature):
    def __init__(self, name, x, y, speed=5, radius=20, color=BLUE):
        super().__init__(x, y, speed, radius, color)
        self.name = name

    def update(self, keys, creatures):
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

    def shoot(self, mouse_x, mouse_y, creatures):
        vector = [mouse_x - self.x, mouse_y - self.y]
        vector_size = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        k = 10 / vector_size if vector_size != 0 else 0
        normal_vector = [vector[0] * k, vector[1] * k]
        bullet = Bullet(self.x, self.y, normal_vector)
        creatures.append(bullet)


class Enemy(Creature):
    def __init__(self, x, y, speed=2, radius=10, color=RED):
        super().__init__(x, y, speed, radius, color)
        self.direction_vector = [0, 0]
        self.last_dir_choose_time = time()
        self.dir_vector_delay = random.randint(16, 24) / 10

    def update(self, keys, creatures):
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


class Bullet(Creature):
    def __init__(self, x, y, dir_vector, speed=10, radius=3, color=BLACK):
        super().__init__(x, y, speed, radius, color)
        self.dir_vector = dir_vector

    def update(self, keys, creatures):
        self.x += self.dir_vector[0]
        self.y += self.dir_vector[1]

        for creature in creatures:
            if isinstance(creature, Enemy):
                if distance([self.x, self.y], [creature.x, creature.y]) < self.radius + creature.radius:
                    creature.die()
                    self.die()
                    break


def main():
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    hero = Hero('Bob', 300, 400, 5)
    creatures = [
        hero,
        Enemy(100, 100),
        Enemy(700, 500),
        Enemy(500, 300),
        Enemy(200, 400),
    ]

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
                hero.shoot(mouse_coords[0], mouse_coords[1], creatures)

        keys = pygame.key.get_pressed()

        screen.fill(WHITE)

        for creature in creatures:
            if creature.is_alive:
                creature.update(keys, creatures)

        for creature in creatures:
            if creature.is_alive:
                creature.draw(screen)

        creatures = [creature for creature in creatures if creature.is_alive]  # creatures = list(filter(lambda creature: creature.is_alive), creatures)

        pygame.display.flip()
        clock.tick(FPS)


main()
