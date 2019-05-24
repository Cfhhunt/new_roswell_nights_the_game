import pygame

class Projectile:
    def __init__(self):
        raise NotImplementedError('Do not create raw Projectile!')

class SmallBullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 30
        self.dmg = 10

class SampleProjectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
