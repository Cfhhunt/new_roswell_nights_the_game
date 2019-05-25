from player import Cassie
import weapons
import ammo
import pygame
import enemies
pygame.init()

# Display and world info
screenWidth = 1920
screenHeight = 1080
win = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption('New Roswell Nights')
bg = pygame.image.load('images\\background.png')
clock = pygame.time.Clock()

def redrawGameWindow():
    win.blit(bg, (0, 0)) #this will eventually be passed to world.draw()
    cassie.draw(win)
    drawProjectiles()
    drawBadGuys()
    pygame.display.update()

def drawProjectiles():
    for projectile in projectiles: # move or remove projectiles
        if projectile.x < screenWidth and projectile.x > 0:
            projectile.x += projectile.vel * projectile.direction
        else:
            projectiles.pop(projectiles.index(projectile))
        projectile.updatePos(cassie.x, cassie.y, cassie.direction)
        projectile.draw(win)

def drawBadGuys():
    for badGuy in badGuys:
        badGuy.draw(win)
        if badGuy.ded:
            badGuys.pop(badGuys.index(badGuy))

cassie = Cassie(250, 880)
badGuys = []
badGuys.append(enemies.Enemy(1100, 880, 250, 200, 1920))
projectiles = []
while not cassie.ded:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if keys[pygame.K_f]:
        if len(projectiles) < 5:
            projectiles.append(cassie.weapon.fire(round(cassie.x + cassie.width //2), round(cassie.y + cassie.height//2), cassie.direction))

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
            cassie.y -= (cassie.jumpCount ** 2) * 0.5 * neg
            cassie.jumpCount -= 1
        else:
            cassie.jumping = False
            cassie.jumpCount = 10
    redrawGameWindow()

pygame.quit()
