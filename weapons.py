import pygame
import ammo

class Weapon:
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapon!')

class PlazmaGun(Weapon):
    def __init__(self):
        self.ammo = ammo.TwoHandPlazma
        self.maxAmmo = 1000
        self.ammoLeft = 1000
        self.duration = 60 # Duration in frames

    def fire(self, x, y, direction):
        return self.ammo(x, y, direction)
