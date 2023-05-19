import pygame
import math

pygame.init()
win = pygame.display.set_mode((1100,250))
pygame.display.set_caption('first game')
clock = pygame.time.Clock()



bg = pygame.image.load('bg2.png')
bg = pygame.transform.scale(bg, (550, 250))

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
        self.down = False
        self.up = False
        self.standing = True
        self.fire = False
        self.hitbox = (self.x + 20, self.y, 28, 60)


        self.vel = 20
        self.walkCount = 0

    def draw(self, win):
        win.blit(king_right[0], (self.x, self.y))
        if self.walkCount >= 3:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(king_left[self.walkCount], (self.x, self.y))
                self.walkCount +=1
            elif self.right:
                win.blit(king_right[self.walkCount], (self.x, self.y))
                self.walkCount +=1
            elif self.up:
                win.blit(king_up[self.walkCount], (self.x, self.y))
                self.walkCount +=1
            elif self.down:
                win.blit(king_down[self.walkCount], (self.x, self.y))
                self.walkCount +=1

        else:
            if self.left:
                win.blit(king_left[0], (self.x, self.y))
            elif self.right:
                win.blit(king_right[0], (self.x, self.y))
            elif self.up:
                win.blit(king_up[0], (self.x, self.y))
            elif self.down:
                win.blit(king_down[0], (self.x, self.y))
        self.hitbox = (self.x + 18, self.y + 20, 40, 85)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class animation_firefireball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fire = False
        self.vel = 5
        self.walkcount = 0


    def fireball(self, win):
        fireball_list = [pygame.image.load('fireball_1.png'),
                         pygame.image.load('fireball_1.png'),
                         pygame.image.load('fireball_1.png'),
                         pygame.image.load('fireball_2.png'),
                         pygame.image.load('fireball_2.png'),
                         pygame.image.load('fireball_2.png')]
        if self.walkcount >=6:
            self.walkcount = 0
        if self.fire == True:
            win.blit(fireball_list[self.walkcount], (self.x + 20, self.y))
            self.walkcount +=1
            self.x += self.vel




class slime(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.vel = 0
        self.alive = True
        self.walkcount = 0
        self.hitbox = (self.x + 20, self.y, 28, 60)
        
        
    

    def draw(self, win):
        slime_list = [
        pygame.image.load('slime_movement_1.png').convert_alpha(),
        pygame.image.load('slime_movement_1.png').convert_alpha(),
        pygame.image.load('slime_movement_1.png').convert_alpha(),
        pygame.image.load('slime_movement_2.png').convert_alpha(),
        pygame.image.load('slime_movement_2.png').convert_alpha(),
        pygame.image.load('slime_movement_2.png').convert_alpha()
        ]
        the_slime = pygame.transform.scale(slime_list[0], (128, 128))
        if self.walkcount >=6:
            self.walkcount = 0

        if self.alive == True:
            the_slime = pygame.transform.scale(slime_list[self.walkcount], (128, 128))
            win.blit(the_slime, (self.x, self.y))
            if self.walkcount == 3:
                self.vel += 8
            else: 
                self.vel = 0
            self.x -= self.vel
            self.walkcount += 1

            

            if self.x < 600:
                self.alive = False

        else:
            self.alive = False
        self.hitbox = (self.x+30, self.y +40, 80, 40)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            

        

character = player(20, 130, 64, 64)
enemy = slime(1000, 140, 64, 64)



def redrawGameWindow(animation):
    count = 1
    
    for i in range(0, tiles):
        win.blit(bg, (i * bg_width ,0))
        count +=1

    character.draw(win)
    enemy.draw(win)
    if animation == True:
        fire_attack.fireball(win)
    

    pygame.display.update()

animation = False
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
        character.up = False
        character.down = False
        character.standing = False

    elif keys[pygame.K_RIGHT]:
        character.x += character.vel
        character.right = True
        character.left = False
        character.up = False
        character.down = False
        character.standing = False

    elif keys[pygame.K_DOWN]:
        character.y += character.vel
        character.right = False
        character.left = False
        character.up = False
        character.down = True
        character.standing = False

    elif keys[pygame.K_UP]:
        character.y -= character.vel
        character.right = False
        character.left = False
        character.up = True
        character.down = False
        character.standing = False


    elif keys[pygame.K_SPACE]:
        animation = True
        fire_attack = animation_firefireball(character.x + 10, character.y + 40, 64,64)
        fire_attack.fire = True
          
    else:
        character.standing = True
        character.walkCount = 0



    redrawGameWindow(animation)