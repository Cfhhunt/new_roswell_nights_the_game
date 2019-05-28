import pygame

class Ammo:
    def __init__(self):
        raise NotImplementedError('Do not create raw Ammo!')

    def updatePos(self, x, y, direction):
        pass

class TwoHandPlazma(Ammo):
    def __init__(self, x, y, direction, duration):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 20
        self.duration = duration
        self.style = 'timed'

    def draw(self, win):
        pygame.draw.rect(win, (0, 220, 255), pygame.Rect(self.x, self.y, 1920 * self.direction, 10))

    def update(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.duration -= 1

class Cal37(Ammo):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 20
        self.style = 'slug'

    def draw(self, win):
        pass
