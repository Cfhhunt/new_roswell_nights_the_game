import pygame

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.walkRight = [pygame.image.load('images\\cassie\\R1.png'), pygame.image.load('images\\cassie\\R2.png'), pygame.image.load('images\\cassie\\R3.png'), pygame.image.load('images\\cassie\\R4.png'), pygame.image.load('images\\cassie\\R5.png'), pygame.image.load('images\\cassie\\R6.png'), pygame.image.load('images\\cassie\\R7.png'), pygame.image.load('images\\cassie\\R8.png')]
        self.walkLeft = [pygame.image.load('images\\cassie\\L1.png'), pygame.image.load('images\\cassie\\L2.png'), pygame.image.load('images\\cassie\\L3.png'), pygame.image.load('images\\cassie\\L4.png'), pygame.image.load('images\\cassie\\L5.png'), pygame.image.load('images\\cassie\\L6.png'), pygame.image.load('images\\cassie\\L7.png'), pygame.image.load('images\\cassie\\L8.png')]
        self.jumpRight = [pygame.image.load('images\\cassie\\JR1.png'), pygame.image.load('images\\cassie\\JR2.png')]
        self.jumpLeft = [pygame.image.load('images\\cassie\\JL1.png'), pygame.image.load('images\\cassie\\JL2.png')]
        self.cassStanding = pygame.image.load('images\\cassie\\S1.png')

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.isJump and self.left:
            if self.jumpCount <= 0:
                win.blit(self.jumpLeft[0], (self.x, self.y))
            else:
                win.blit(self.jumpLeft[1], (self.x, self.y))
        elif self.isJump:
            if self.jumpCount <= 0:
                win.blit(self.jumpRight[0], (self.x, self.y))
            else:
                win.blit(self.jumpRight[1], (self.x, self.y))
        elif self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.cassStanding, (self.x, self.y))
