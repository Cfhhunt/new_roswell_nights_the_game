import pygame

class Munitions:
    def __init__(self):
        raise NotImplementedError('Do not create raw Ammo!')

    def updatePos(self, x, y, direction):
        pass

class ACP45(Munitions):
    def __init__(self, x, y, direction):
        self.type = 'slug'
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 25
        self.dmg = 10
        self.done = False

    def update(self):
        self.x += (self.direction * self.vel)

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 10)

    def hitCheck(self, hitBox):
        enemyX, enemyY, maxX, maxY = hitBox
        if self.x > enemyX and self.x < enemyX + maxX:
            if self.y > enemyY and self.y < enemyY + maxY:
                self.done = True
                return True
        return False

class MeleeStrike(Munitions):
    def __init__(self, x, y, direction):
        self.type = 'melee'
        self.x = x
        self.y = y
        self.direction = direction
        self.dmg = 15
        self.reach = 50

    def update(self):
        pass

    def draw(self, win):
        pass
