import pygame

class Enemy(object):
    walkRight = [pygame.image.load('images\\cassie\\S1.png')] # Add animations
    walkLeft = [pygame.image.load('images\\cassie\\S1.png')] # Add animations

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 7
        self.path = [self.x, self.end]
        self.hp = 20
        self.maxHp = 20
        self.ded = False
        self.walkRight = [pygame.image.load('images\\pallene\\S1.png')] # Add animations
        self.walkLeft = [pygame.image.load('images\\pallene\\S1.png')] # Add animations
        self.hitBox = (self.x + 50, self.y, 100, 100)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 <= 24:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[0], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[0], (self.x, self.y))
            self.walkCount += 1
        self.hitBox = (self.x + 50, self.y, 100, 100)
        if self.hp <= 0:
            self.ded = True

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
