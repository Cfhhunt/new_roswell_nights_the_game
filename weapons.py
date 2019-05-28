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
        self.maxCoolDown = 180 # Time between firing, need a general 'fire style' info
        self.coolDown = self.maxCoolDown
        self.Down = 30
        self.fired = False
        self.weaponType = 'twoHand'

    def fire(self, x, y, direction):
        return self.ammo(x, y, direction, self.duration)
        self.ammoLeft -= duration
        self.fired = True

    def update(self):
        if self.fired == True:
            self.coolDown -= 1
        if self.coolDown <= 0:
            self.fired = False
            self.coolDown = self.maxCoolDown
