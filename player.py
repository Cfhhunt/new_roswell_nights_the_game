import weapons
import pygame

class Player:
    def __init__(self):
        raise NotImplementedError('Do not create raw Character!')

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.jumping and self.direction == -1:
            if self.jumpCount <= 0:
                win.blit(self.jumpLeft[0], (self.x, self.y))
            else:
                win.blit(self.jumpLeft[1], (self.x, self.y))
        elif self.jumping:
            if self.jumpCount <= 0:
                win.blit(self.jumpRight[0], (self.x, self.y))
            else:
                win.blit(self.jumpRight[1], (self.x, self.y))
        elif not self.moving:
            win.blit(self.standing, (self.x, self.y))
        elif self.direction == -1:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        self.hitBox = (self.x + 50, self.y, 100, 100)
        if self.hp <= 0:
            self.ded = True

class Cassie(Player):
    def __init__(self, x, y):
        self.name = 'Cassandra McQueen'
        self.x = x
        self.y = y
        self.width = 250
        self.height = 250
        self.vel = 10
        self.jumping = False
        self.jumpCount = 10
        self.direction = 1
        self.walkCount = 0
        self.moving = False
        self.attacking = False
        self.stunned = False
        self.ded = False

        self.hp = 100
        self.maxHp = 100
        self.hitBox = (self.x + 50, self.y, 100, 100)
        self.weapon = weapons.PlazmaGun()

        # Sprites
        self.walkRight = [pygame.image.load('images\\cassie\\R1.png'), pygame.image.load('images\\cassie\\R2.png'), pygame.image.load('images\\cassie\\R3.png'), pygame.image.load('images\\cassie\\R4.png'), pygame.image.load('images\\cassie\\R5.png'), pygame.image.load('images\\cassie\\R6.png'), pygame.image.load('images\\cassie\\R7.png'), pygame.image.load('images\\cassie\\R8.png')]
        self.walkLeft = [pygame.image.load('images\\cassie\\L1.png'), pygame.image.load('images\\cassie\\L2.png'), pygame.image.load('images\\cassie\\L3.png'), pygame.image.load('images\\cassie\\L4.png'), pygame.image.load('images\\cassie\\L5.png'), pygame.image.load('images\\cassie\\L6.png'), pygame.image.load('images\\cassie\\L7.png'), pygame.image.load('images\\cassie\\L8.png')]
        self.jumpRight = [pygame.image.load('images\\cassie\\JR1.png'), pygame.image.load('images\\cassie\\JR2.png')]
        self.jumpLeft = [pygame.image.load('images\\cassie\\JL1.png'), pygame.image.load('images\\cassie\\JL2.png')]
        self.standing = pygame.image.load('images\\cassie\\S1.png')


class Shespoz(Player):
    def __init__(self, x, y):
        self.name = 'Lian Shespoz'
        self.x = x
        self.y = y
        self.width = 250
        self.height = 250
        self.vel = 10
        self.jumping = False
        self.jumpCount = 10
        self.direction = 1
        self.walkCount = 0
        self.standing = True
        self.attacking = False
        self.stunned = False
        self.ded = False
        self.walkRight = [pygame.image.load('images\\cassie\\R1.png'), pygame.image.load('images\\cassie\\R2.png'), pygame.image.load('images\\cassie\\R3.png'), pygame.image.load('images\\cassie\\R4.png'), pygame.image.load('images\\cassie\\R5.png'), pygame.image.load('images\\cassie\\R6.png'), pygame.image.load('images\\cassie\\R7.png'), pygame.image.load('images\\cassie\\R8.png')]
        self.walkLeft = [pygame.image.load('images\\cassie\\L1.png'), pygame.image.load('images\\cassie\\L2.png'), pygame.image.load('images\\cassie\\L3.png'), pygame.image.load('images\\cassie\\L4.png'), pygame.image.load('images\\cassie\\L5.png'), pygame.image.load('images\\cassie\\L6.png'), pygame.image.load('images\\cassie\\L7.png'), pygame.image.load('images\\cassie\\L8.png')]
        self.jumpRight = [pygame.image.load('images\\cassie\\JR1.png'), pygame.image.load('images\\cassie\\JR2.png')]
        self.jumpLeft = [pygame.image.load('images\\cassie\\JL1.png'), pygame.image.load('images\\cassie\\JL2.png')]
        self.standing = pygame.image.load('images\\cassie\\S1.png')
        self.weapon = weapons.PlazmaGun()
