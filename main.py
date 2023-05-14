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
black = (0,0,0)

scroll = 0
sprite_sheet_image = pygame.image.load('knights.png').convert_alpha()





class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey(colour)

        return image
    
    def get_image_2(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 110, width , 120))
        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey(colour)

        return image
    
    def get_image_3(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 220, width , 120))
        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey(colour)

        return image
    
    def get_image_4(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 330, width , 120))
        image = pygame.transform.scale(image, (width, height))
        image.set_colorkey(colour)

        return image
    



image_count = 0  


king_down = []
king_left = []
king_right = []
king_up = []


knight_down = []
knight_left = []
knight_right = []
knight_up = []


knight_black_down = []
knight_black_left = []
knight_black_right = []
knight_black_up = []


knight_green_down = []
knight_green_left = []
knight_green_right = []
knight_green_up = []


down_animations_list = [king_down, knight_down, knight_black_down, knight_green_down]
left_animations_list = [king_left, knight_left, knight_black_left, knight_green_left]
right_animations_list = [king_right, knight_right, knight_black_right, knight_green_right]
up_animations_list = [king_up, knight_up, knight_black_up, knight_green_up]

for i in down_animations_list:
    for j in range(3):
        i.append(SpriteSheet(sprite_sheet_image).get_image(image_count, 79, 110, 3, black))
        image_count+=1
image_count = 0  

for i in left_animations_list:
    for j in range(3):
        i.append(SpriteSheet(sprite_sheet_image).get_image_2(image_count, 79, 220, 3, black))
        image_count+=1
image_count = 0  

for i in right_animations_list:
    for j in range(3):
        i.append(SpriteSheet(sprite_sheet_image).get_image_3(image_count, 79, 220, 3, black))
        image_count+=1
image_count = 0  

for i in up_animations_list:
    for j in range(3):
        i.append(SpriteSheet(sprite_sheet_image).get_image_4(image_count, 79, 330, 3, black))
        image_count+=1
image_count = 0  
  

    
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
        win.blit(king_up[0], (self.x, self.y))



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