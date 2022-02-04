from Classes.game_object import GameObject


class Creature(GameObject):
    side = None  # фракция, к которой относится существо

    def __init__(self, x, y, speed: float, radius, color):
        super().__init__(x, y, radius, color)
        self.speed = speed
