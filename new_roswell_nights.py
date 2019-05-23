import pygame
pygame.init()

screenWidth = 1920
screenHeight = 1080

win = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption('New Roswell Nights')

walkRight = [pygame.image.load('images\\R1.png'), pygame.image.load('images\\R2.png'), pygame.image.load('images\\R3.png'), pygame.image.load('images\\R4.png'), pygame.image.load('images\\R5.png'), pygame.image.load('images\\R6.png'), pygame.image.load('images\\R7.png'), pygame.image.load('images\\R8.png')]
walkLeft = [pygame.image.load('images\\L1.png'), pygame.image.load('images\\L2.png'), pygame.image.load('images\\L3.png'), pygame.image.load('images\\L4.png'), pygame.image.load('images\\L5.png'), pygame.image.load('images\\L6.png'), pygame.image.load('images\\L7.png'), pygame.image.load('images\\L8.png')]
jumpRight = [pygame.image.load('images\\JR1.png'), pygame.image.load('images\\JR2.png')]
jumpLeft = [pygame.image.load('images\\JL1.png'), pygame.image.load('images\\JL2.png')]
bg = pygame.image.load('images\\background.png')
cassStanding = pygame.image.load('images\\S1.png')

clock = pygame.time.Clock()

class player(object):
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

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.isJump and self.left:
            if self.jumpCount <= 0:
                win.blit(jumpLeft[0], (self.x, self.y))
            else:
                win.blit(jumpLeft[1], (self.x, self.y))
        elif self.isJump:
            if self.jumpCount <= 0:
                win.blit(jumpRight[0], (self.x, self.y))
            else:
                win.blit(jumpRight[1], (self.x, self.y))
        elif self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(cassStanding, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg, (0, 0))
    cassie.draw(win)
    pygame.display.update()

cassie = player(250, 880, 250, 200)
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        pygame.quit()

    if keys[pygame.K_LEFT] and cassie.x > 0:
        cassie.x -= cassie.vel
        cassie.left = True
        cassie.right = False
    elif keys[pygame.K_RIGHT] and cassie.x < screenWidth - cassie.width:
        cassie.x += cassie.vel
        cassie.left = False
        cassie.right = True
    else:
        cassie.left = False
        cassie.right = False
        cassie.walkCount = 0
    if not(cassie.isJump):
        if keys[pygame.K_SPACE]:
            cassie.isJump = True
            cassie.right = True
            cassie.left = False
            cassie.walkCount = 0
    else:
        if cassie.jumpCount >= -10:
            neg = 1
            if cassie.jumpCount < 0:
                neg = -1
            cassie.y -= (cassie.jumpCount ** 2) * 0.5 * neg
            cassie.jumpCount -= 1
        else:
            cassie.isJump = False
            cassie.jumpCount = 10
    redrawGameWindow()

pygame.quit()
