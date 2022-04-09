import pygame
pygame.init()
screen_width = 800
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))
# walkRight = [pygame.image.load('Pygame-Tutorials/Game/R1.png'), pygame.image.load('Pygame-Tutorials/Game/R2.png'), pygame.image.load('Pygame-Tutorials/Game/R3.png'), pygame.image.load('Pygame-Tutorials/Game/R4.png'), pygame.image.load('Pygame-Tutorials/Game/R5.png'), pygame.image.load('Pygame-Tutorials/Game/R6.png'), pygame.image.load('Pygame-Tutorials/Game/R7.png'), pygame.image.load('Pygame-Tutorials/Game/R8.png'), pygame.image.load('Pygame-Tutorials/Game/R9.png')]
# walkLeft = [pygame.image.load('Pygame-Tutorials/Game/L1.png'), pygame.image.load('Pygame-Tutorials/Game/L2.png'), pygame.image.load('Pygame-Tutorials/Game/L3.png'), pygame.image.load('Pygame-Tutorials/Game/L4.png'), pygame.image.load('Pygame-Tutorials/Game/L5.png'), pygame.image.load('Pygame-Tutorials/Game/L6.png'), pygame.image.load('Pygame-Tutorials/Game/L7.png'), pygame.image.load('Pygame-Tutorials/Game/L8.png'), pygame.image.load('Pygame-Tutorials/Game/L9.png')]
walkLeft = [pygame.image.load('L%s.png'%frame) for frame in range(1,10)]
walkRight = [pygame.image.load('R%s.png'%frame) for frame in range(1,10)]

bg = pygame.image.load('bg.jpg')
cha = pygame.image.load('standing.png')

pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

x = 200
y = 416
width = 64 # the hitbox has to match the dimension of the character 
height = 64 # the hitbox has to match the dimension of the character
vel = 4


isJump = False
jumpCount = 10
left = False
right = False
walkcount = 0

def redrawGameWindow():
    global walkcount
   
    win.blit(bg, (0,0))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # if walkcount + 1 > 27:
    #     walkcount = 0

    # if left:
    #     win.blit(walkLeft[walkcount//3], (x,y))
    #     walkcount += 1

    # elif right:
    #     win.blit(walkRight[walkcount//3], (x,y))
    #     walkcount += 1
    if left:
        win.blit(walkLeft[walkcount], (x,y))
        walkcount = (walkcount + 1) % 9

    elif right:
        win.blit(walkRight[walkcount], (x,y))
        walkcount = (walkcount + 1) % 9

    else:
        win.blit(cha, (x,y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False 
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < screen_width - width - vel: # try 'if' here
           x += vel
           right = True
           left = False

    elif keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
    
    else:
            right = False
            left = False
            walkCount = 0

    if not isJump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < screen_height - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            # neg = 1
            # if jumpCount < 0:
            #     neg = -1
            # y -= (jumpCount ** 2) * 0.5 * neg
            y -= (jumpCount * abs(jumpCount)) * 0.5 
            jumpCount -= 1
        else: 
            isJump = False
            jumpCount = 10

    redrawGameWindow()
                
    # for event in pygame.key.get_pressed():
    #     if event == pygame.K_RIGHT:
    #         x += vel
    #     if event == pygame.K_LEFT:
    #         x -= vel
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_
    
pygame.quit()