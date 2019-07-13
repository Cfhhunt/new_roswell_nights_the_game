from player import Cassie
from world import World
import weapons
import munitions
import pygame
import enemies
pygame.init()

# TODO: Figure out what you want from this game
# TODO: make background move with player
# TODO: Write out skeleton code
# TODO: START COMMENTING YOUR CODE!!!

# Display and world info
screenWidth = 1920
screenHeight = 1080
paused = False
win = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption('New Roswell Nights')
bg = pygame.image.load('images\\background.png')
clock = pygame.time.Clock()
world = World(win, screenWidth, screenHeight)

pygame.font.init() # you have to call this at the start, if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def redrawGameWindow(): # Order should be world, cassie, badGuys, projectiles
    world.draw(win, cassie)
    drawPlayer()
    drawBadGuys()
    drawProjectiles()
    win.blit(textsurface,(0,0))
    pygame.display.update()

def drawPlayer():
    cassie.update()
    cassie.draw(win)

def drawBadGuys(): # update, draw, pop
    for badGuy in badGuys:
        badGuy.update()
        badGuy.draw(win)
        if badGuy.ded:
            badGuys.pop(badGuys.index(badGuy))

def drawProjectiles(): # update, draw, hitCheck, pop
    for projectile in projectiles:
        projectile.update()
        projectile.draw(win)
        for badGuy in badGuys:
            projectile.hitCheck(badGuy, badGuy.hitBox)
            if projectile.done:
                projectiles.pop(projectiles.index(projectile))


cassie = Cassie(250, 840)
badGuys = []
badGuys.append(enemies.Enemy(1100, 880, 250, 200, 1920))
projectiles = []

while not cassie.ded:
    clock.tick(48)
    textsurface = myfont.render(str(clock.get_fps()) + '\nHealth: ' + str(cassie.hp) , False, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]: # Pause button
        if paused:
            paused = False
        else:
            paused = True
        pygame.time.wait(500)

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if paused:
        continue

    # ALL PLAYER MOVEMENT/ACTIONS AND RELATED LOGIC IS DONE HERE
    if cassie.canAttack():
        if keys[pygame.K_f]:
            if cassie.oneHand.canFire():
                projectiles.append(cassie.oneHand.fire(cassie.handPosX, cassie.handPosY, cassie.direction))
        if keys[pygame.K_d]:
            if cassie.melee.canFire():
                projectiles.append(cassie.melee.fire(cassie.handPosX, cassie.handPosY, cassie.direction))

    if keys[pygame.K_LEFT] and cassie.x > 0:
        cassie.x -= cassie.vel
        cassie.direction = -1
        cassie.moving = True
    elif keys[pygame.K_RIGHT] and cassie.x < screenWidth - cassie.width:
        cassie.x += cassie.vel
        cassie.direction = 1
        cassie.moving = True
    else:
        cassie.moving = False
        cassie.walkcount = 0
    if not cassie.jumping:
        if keys[pygame.K_SPACE]:
            cassie.jumping = True
            cassie.walkCount = 0
    else:
        if cassie.jumpCount >= -10:
            neg = 1
            if cassie.jumpCount < 0:
                neg = -1
            cassie.y -= (cassie.jumpCount ** 2) //2 * neg
            cassie.jumpCount -= 1
        else:
            cassie.jumping = False
            cassie.jumpCount = 10
    redrawGameWindow()

pygame.quit()
