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
