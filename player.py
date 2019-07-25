import weapons
import pygame

# Player class
class Player:
    # Initialization. start the player in the lower left corner of the screen
    def __init__(self):
        pass

    def update(): # Make changes based on user input and world Info
        # check if dead
        # update status effects
        # call move()
        # update attack info
        pass

    def draw(): # Choose a sprite based on what the player is doing
        pass

    def fire(): # Fire one of three weapons based on key pressed.
        pass

    def move():
        pass

class Cassie(Player):
    def __init__(self, x, y):
        self.name = 'Cassandra McQueen'

        # state
        self.x = x
        self.y = y
        self.width = 250
        self.height = 250
        self.mass = 1
        self.vel = 10
        self.isJumping = False
        self.direction = 1
        self.moving = False
        self.ded = False

        # sprites
        self.walkRight = [pygame.image.load('images\\cassie\\R1.png'), pygame.image.load('images\\cassie\\R2.png'), pygame.image.load('images\\cassie\\R3.png'), pygame.image.load('images\\cassie\\R4.png'), pygame.image.load('images\\cassie\\R5.png'), pygame.image.load('images\\cassie\\R6.png'), pygame.image.load('images\\cassie\\R7.png'), pygame.image.load('images\\cassie\\R8.png')]
        self.walkLeft = [pygame.image.load('images\\cassie\\L1.png'), pygame.image.load('images\\cassie\\L2.png'), pygame.image.load('images\\cassie\\L3.png'), pygame.image.load('images\\cassie\\L4.png'), pygame.image.load('images\\cassie\\L5.png'), pygame.image.load('images\\cassie\\L6.png'), pygame.image.load('images\\cassie\\L7.png'), pygame.image.load('images\\cassie\\L8.png')]
        self.jumpRight = [pygame.image.load('images\\cassie\\JR1.png'), pygame.image.load('images\\cassie\\JR2.png')]
        self.jumpLeft = [pygame.image.load('images\\cassie\\JL1.png'), pygame.image.load('images\\cassie\\JL2.png')]
        self.standing = [pygame.image.load('images\\cassie\\S1.png'), pygame.image.load('images\\cassie\\S1.png')]

    # All movement and state update go in here
    def update(self, keys):
        pass
