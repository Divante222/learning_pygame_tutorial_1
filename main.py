import pygame
import math

pygame.init()
win = pygame.display.set_mode((1100,250))
pygame.display.set_caption('first game')
clock = pygame.time.Clock()



bg = pygame.image.load('bg.png')

bg_width = bg.get_width()
bg_height = bg.get_height()
tiles = math.ceil(1000 / bg_width)


scroll = 0
standing = pygame.image.load('standing.jpg')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.vel = 20

    def draw(self, win):
        win.blit(standing, (self.x, self.y))


character = player(20, 100, 64, 64)

def redrawGameWindow():
    count = 1
    for i in range(0, tiles):
        win.blit(bg, (i * bg_width ,0))
        count +=1

    character.draw(win)

    pygame.display.update()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    clock.tick(27)
    if keys[pygame.K_LEFT]:
        character.x -= character.vel
        character.left = True
        character.right = False

    elif keys[pygame.K_RIGHT]:
        character.x += character.vel
        character.right = True
        character.left = False
    elif keys[pygame.K_DOWN]:
        character.y += character.vel

    elif keys[pygame.K_UP]:
        character.y -= character.vel



    redrawGameWindow()