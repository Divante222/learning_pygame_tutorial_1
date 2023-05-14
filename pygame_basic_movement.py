import pygame 
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('first game')

x = 50 
y = 50
width = 40 
height = 60
vel = 5
screenWidth = 500

is_jump = False
jump_count = 10


run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - 5:
         x += vel
    if not(is_jump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenWidth - height - 5:
            y+= vel
        if keys[pygame.K_SPACE]:
                is_jump = True
    else:
        if jump_count >= -10: 
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count **2) * .5  * neg
            jump_count -=1

        else:
             is_jump = False
             jump_count = 10


    win.fill((0,0,0))    
    pygame.draw.rect(win, (255, 0, 0), (x,y,width, height))
    pygame.display.update()


pygame.quit()
