from player import Cassie
from world import World
import weapons
import munitions
import pygame
import enemies
pygame.init()

# TODO: SKELETON CODE
# TODO: clean out all code thats not about movement/drawing
# TODO: Update movement code in while loop
# TODO: rework action code with a switch statement
# TODO: allow both cassie and enemies to take damage

# Display and world info
screenWidth = 1920
screenHeight = 1080
win = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption('New Roswell Nights')
bg = pygame.image.load('images\\background.png')
clock = pygame.time.Clock()
world = World(win, screenWidth, screenHeight)

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)



def redrawGameWindow():
    #win.blit(bg, (0, 0)) #this will eventually be passed to world.draw()
    world.update(win, cassie)
    world.draw(win)
    cassie.update() # Run the update loop
    updateProjectiles()
    hitCheck()
    updateBadGuys()
    cassie.draw(win) # draw based on state
    drawProjectiles()
    drawBadGuys()
    win.blit(textsurface,(0,0))
    pygame.display.update()

def updateProjectiles():
    for projectile in projectiles:
        #if done, delete
        projectile.update()

def drawProjectiles():
    for projectile in projectiles:
        projectile.draw(win)

def updateBadGuys(): #pass info about world to badguys
    for badGuy in badGuys:
        badGuy.update()
        if badGuy.ded:
            badGuys.pop(badGuys.index(badGuy))

def drawBadGuys():
    for badGuy in badGuys:
        badGuy.draw(win)

def hitCheck(): #check for hit, do damage, delete projectile
    for projectile in projectiles:
        for badGuy in badGuys:
            if projectile.hitCheck(badGuy.hitBox) == True:
                badGuy.hp = badGuy.hp - projectile.dmg
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

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

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
