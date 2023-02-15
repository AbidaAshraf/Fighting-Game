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
    
    players.update()
    players.draw(screen)
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
