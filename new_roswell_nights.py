from player import Player
from enemies import Enemy
from projectiles import SampleProjectile
import pygame
pygame.init()

screenWidth = 1920
screenHeight = 1080

win = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption('New Roswell Nights')

bg = pygame.image.load('images\\background.png')

clock = pygame.time.Clock()

def redrawGameWindow():
    win.blit(bg, (0, 0))
    cassie.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

cassie = Player(250, 880, 250, 200)
enemy = Enemy(1100, 880, 250, 200, 1920)
bullets = []
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if cassie.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(SampleProjectile(round(cassie.x + cassie.width //2), round(cassie.y + cassie.height//2), 6, (0,220,255), facing))

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
