import pygame
import munitions

class Weapon:
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapon!')

class ColtSAA(Weapon):
    def __init__(self):
        self.name = 'Colt Single Action Army'
        self.type = 'oneHand'
        self.maxAmmo = 12
        self.ammo = self.maxAmmo
        self.munition = munitions.ACP45
        self.coolDown = 0
        self.coolDuration = 7

    def fire(self, x, y, direction):
        self.coolDown = self.coolDuration
        self.ammo -= 1
        return self.munition(x, y, direction)

    def update(self):
        if self.coolDown > 0:
            self.coolDown -= 1

    def canFire(self):
        return self.coolDown == 0 and self.ammo > 0

class TireIron(Weapon):
    def __init__(self):
        self.name = 'Tire Iron'
        self.type = 'melee'
        self.munition = munitions.MeleeStrike
        self.coolDown = 0
        self.coolDuration = 7

    def fire(self, x, y, direction):
        return self.munition(x, y, direction)

    def update(self):
        if self.coolDown > 0:
            self.coolDown -= 1

    def canFire(self):
        return self.coolDown == 0
