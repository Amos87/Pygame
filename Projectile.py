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

class Enemy(object):
    walkRight = [pygame.image.load(f'Sprites/R{frame}E.png') for frame in range(1,12)]
    walkLeft = [pygame.image.load(f'Sprites/L{frame}E.png') for frame in range(1,12)]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        #self.hitbox = (self.x + 13, self.y, 40, 60)

    def draw(self, win):
        self.move()
        # if self.walkCount + 1 >= 33:
        #     self.walkCount = 0

        if self.vel > 0:  #whether self.vel is negative or positive
            win.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount = (self.walkCount + 1) % 11
        else:
            win.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount = (self.walkCount + 1) % 11
        self.hitbox = (self.x + 13, self.y, 40, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                #self.walkCount = 0

        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                #self.walkCount = 0

    # function for when alien or globin is hit then print.
    def hit(self):
        print('hit')


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
        self.walkcount = 0
        self.standing = True
        #self.hitbox = (self.x + 13, self.y + 7, 40, 60)

    def draw(self, win):

        if not self.standing:
            
            if self.right:
                win.blit(walkRight[self.walkcount], (self.x, self.y))
                self.walkcount = (self.walkcount + 1) % 9

            elif self.left:
                win.blit(walkLeft[self.walkcount], (self.x, self.y))
                self.walkcount = (self.walkcount + 1) % 9

        else:

            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
                
            elif self.right:
                win.blit(walkRight[0], (self.x, self.y))
            
            else:
                win.blit(cha, (self.x, self.y))
        self.hitbox = (self.x + 13, self.y + 7, 40, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5 * self.facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    globin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    


man = Player(300, 410, 64, 64)
globin = Enemy(100, 410, 64, 64, 500)
bullets = []
shootloop = 0  #timer to fire bullets.
run = True
while run:
    clock.tick(33)
     #setting a timer so that its one bullet that comes out at a time.
    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False 
    
    
    for bullet in bullets:
        #checks to see if bullets is above the buttom of the rectangle & below the top of the rectangle.
        if bullet.y - bullet.radius < globin.hitbox[1] + globin.hitbox[3] and bullet.y + bullet.radius > globin.hitbox[1]: 
            # right side of the left side of the rectangle.
            if bullet.x + bullet.radius > globin.hitbox[0] and bullet.x - bullet.radius < globin.hitbox[0] + globin.hitbox[2]:
                # globin gets hit
                globin.hit()
                bullets.remove(bullet)
        if bullet.x < screen_width and bullet.x > 0:
             bullet.x += bullet.vel
        
        else:
            #bullets.pop(bullets.index(bullet))
            bullets.remove(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1
        elif man.right:
            facing = 1
        else:
            facing = 1
            
        #this is where an instance/object is created of projectfile class. 
        if len(bullets) < 3:
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 4, (255, 0, 0), facing))
          
        shootloop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel: # try 'if' here
           man.x += man.vel
           man.right = True
           man.left = False
           man.standing = False

    else:
            man.standing = True
            man.walkcount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
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
    
    redrawGameWindow()
    
pygame.quit()
