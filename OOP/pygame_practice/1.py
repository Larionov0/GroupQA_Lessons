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
screen = pygame.display.set_mode([WIDTH, HEIGHT])

x = 300
y = 200

x_dir = 0
y_dir = 0

speed = 5

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

    x += x_dir * speed
    y += y_dir * speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), 30)
    pygame.display.flip()

    clock.tick(60)
