import pygame


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
