#creating an OOP, Class from firstgame.
import pygame
pygame.init()
screen_width = 800
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))
# walkRight = [pygame.image.load('Pygame-Tutorials/Game/R1.png'), pygame.image.load('Pygame-Tutorials/Game/R2.png'), pygame.image.load('Pygame-Tutorials/Game/R3.png'), pygame.image.load('Pygame-Tutorials/Game/R4.png'), pygame.image.load('Pygame-Tutorials/Game/R5.png'), pygame.image.load('Pygame-Tutorials/Game/R6.png'), pygame.image.load('Pygame-Tutorials/Game/R7.png'), pygame.image.load('Pygame-Tutorials/Game/R8.png'), pygame.image.load('Pygame-Tutorials/Game/R9.png')]
# walkLeft = [pygame.image.load('Pygame-Tutorials/Game/L1.png'), pygame.image.load('Pygame-Tutorials/Game/L2.png'), pygame.image.load('Pygame-Tutorials/Game/L3.png'), pygame.image.load('Pygame-Tutorials/Game/L4.png'), pygame.image.load('Pygame-Tutorials/Game/L5.png'), pygame.image.load('Pygame-Tutorials/Game/L6.png'), pygame.image.load('Pygame-Tutorials/Game/L7.png'), pygame.image.load('Pygame-Tutorials/Game/L8.png'), pygame.image.load('Pygame-Tutorials/Game/L9.png')]
walkLeft = [pygame.image.load('Sprites/L%s.png'%frame) for frame in range(1,10)]
walkRight = [pygame.image.load('Sprites/R%s.png'%frame) for frame in range(1,10)]

bg = pygame.image.load('Sprites/bg.jpg')
cha = pygame.image.load('Sprites/standing.png')

pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):

        if self.left:
            win.blit(walkLeft[self.walkcount], (self.x, self.y))
            self.walkcount = (self.walkcount + 1) % 9

        elif self.right:
            win.blit(walkRight[self.walkcount], (self.x, self.y))
            self.walkcount = (self.walkcount + 1) % 9

        else:
            win.blit(cha, (self.x,self.y))
    
    def redrawGameWindow(self, win):
        win.blit(bg, (0,0))
        self.draw(win)
        pygame.display.update()

man = Player(300, 410, 64, 64)


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False 
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel: # try 'if' here
           man.x += man.vel
           man.right = True
           man.left = False

    elif keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
    
    else:
            man.right = False
            man.left = False
            man.walkcount = 0

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5 
            man.jumpCount -= 1
        else: 
            man.isJump = False
            man.jumpCount = 10

    man.redrawGameWindow(win)
    
pygame.quit()