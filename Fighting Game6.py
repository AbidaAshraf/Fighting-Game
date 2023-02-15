import pygame
pygame.init()

#create game wondow
size = (1000,600)
screen  = pygame.display.set_mode(size)
pygame.display.set_caption("Fighting Game")

done = False
clock = pygame.time.Clock()

#create background image
background_position = [0,0]
background_image = pygame.image.load("Game Background.jpg").convert()
background_image = pygame.transform.scale(background_image, (size))
screen.blit(background_image, background_position)

#create player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.move = (x, y)
        self.health = 100

player1 = Player(100,230,"Warrior Idle.png")
player2 = Player(300,200,"Wizard Idle.png")

players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    class enemy(object):
    walkRight = ["Warrior Idle.png"]
    walkLeft = ["Wizard Idle.png"]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10 # NEW
        self.visible = True # NEW

    def draw(self,win):
        self.move()
        if self.visible: # NEW
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # NEW
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # NEW
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self): # ALL NEW
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')
    
    players.update()
    players.draw(screen)
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
