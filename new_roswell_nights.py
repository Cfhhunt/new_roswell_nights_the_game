from player import Cassie
from world import World
import weapons
import munitions
import pygame
import enemies
pygame.init()

# Initialization. Global variables and setting up pygame
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

# create player, badGuys, projectile array, etc.
cassie = Cassie(250, 840)
badGuys = []
projectiles = []
animations = [] # To add later, death/explosion animations

# Update function. Update world, player, badGuys, projectiles.
def update(keys):
    # update world
    world.update(cassie)

    # update player
    cassie.update(keys)

    # update badguys and projectiles
    for badGuy in badGuys:
        badGuy.update(cassie)

    # update projectiles, check for hits, remove if done
    for projectile in projectiles:
        projectile.update()
        for badGuy in badGuys:
            projectile.hitCheck(badGuy)
            if badGuy.ded:
                badGuys.pop(badGuys.index(badGuy))
            if projectile.ded:
                projectiles.pop(projectiles.index(projectile))

# Draw function. This should run every assets individual draw function
def redraw():
    world.draw(win)
    cassie.draw(win)
    for badGuy in badGuys:
        badGuy.draw(win)
    for projectile in projectiles:
        projectile.draw(win)
    win.blit(textsurface, (0, 0))
    pygame.display.update()


# Pause function. If user paused, pause
def pause():
    if paused:
        paused = False
    else:
        paused = True
        pygame.time.wait(500)

# Victory condition
def victory():
    return False

# Game loop. This will first take player input, run all updates, then redraw
while not cassie.ded: # Run this loop as long as the player lives
    clock.tick(48)
    textsurface = myfont.render('_', False, (0, 0, 0))

    # Check for victory condition
    if victory():
        print('You win!') # temp
        pygame.quit()

    # Get user input
    keys = pygame.key.get_pressed()

    # if paused, pause()
    if keys[pygame.K_p]:
        pause()
    if paused:
        continue

    update(keys) # Update all assets

    redraw() # redraw all assets

pygame.quit()
