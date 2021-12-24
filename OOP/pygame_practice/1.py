import pygame
from time import sleep
pygame.init()  # настройка пайгейма

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 500

FPS = 60


class Hero:
    def __init__(self, name, x, y, speed, radius=30, color=BLUE):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color

    def update(self, x_dir, y_dir):
        """
        Метод, который будет вызываться на каждой итерации основного цикла программы
        """
        self.x += x_dir * self.speed
        self.y += y_dir * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


screen = pygame.display.set_mode([WIDTH, HEIGHT])

x_dir = 0
y_dir = 0

heroes = [
    Hero('Bob', 350, 300, 10, 50, BLUE),
    Hero('Bob', 350, 300, 7, 80, (0, 100, 255)),
    Hero('Bob', 350, 300, 5, 100, (0, 150, 200)),
]
heroes.reverse()

clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            direction = event.unicode

            if direction in ('w', 'a', 's', 'd'):
                if direction == 'w':
                    y_dir = -1
                elif direction == 'a':
                    x_dir = -1
                elif direction == 's':
                    y_dir = 1
                elif direction == 'd':
                    x_dir = 1

        if event.type == pygame.KEYUP:
            direction = event.unicode

            if direction in ('w', 'a', 's', 'd'):
                if direction == 'w':
                    y_dir = 0
                elif direction == 'a':
                    x_dir = 0
                elif direction == 's':
                    y_dir = 0
                elif direction == 'd':
                    x_dir = 0

    screen.fill(WHITE)

    for hero in heroes:
        hero.update(x_dir, y_dir)

    for hero in heroes:
        hero.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
