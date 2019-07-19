import pygame

class World:
    def __init__(self, win, screenWidth, screenHeight):
        self.bg = pygame.image.load('images\\background.png').convert()
        # foo = pygame.image.load(PATH).get_rect().size
        self.imageSize = pygame.image.load('images\\background.png').get_rect().size
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.x = 0
        self.y = 0

    def update(self, win, cassie):
        if self.x > -(self.imageSize[0]) + screenWidth:
            if cassie.x > self.screenWidth - 300:
                self.x -= 5
            elif cassie.x < 10 and self.x < 5:
                self.x += 5

    def draw(self, win, player):
        self.update(win, player)
        win.blit(self.bg, (self.x, self.y))
