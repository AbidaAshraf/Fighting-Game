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
        self.health = 100
        self.max_health = 100
        self.health_bar_width = 100
        self.health_bar_height = 10

     def move(self, direction):
        speed = 5
        if direction == "left":
            self.rect.x -= speed
            self.facing_right = False
        elif direction == "right":
            self.rect.x += speed
            self.facing_right = True

    def attack(self, other_player):
        damage = 10
        if self.rect.colliderect(other_player.rect):
            other_player.health -= damage

    def draw_health_bar(self):
        # Draw the player's health bar at the top of the screen
        health_bar_x = self.rect.x
        health_bar_y = self.rect.y - 20
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, self.health_bar_width, self.health_bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, self.health_bar_width * (self.health / self.max_health), self.health_bar_height))

player1 = Player(200,400,"Warrior Idle.png")
player2 = Player(600,365,"Wizard Idle.png")

players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.move("left")
            elif event.key == pygame.K_RIGHT:
                player1.move("right")
            elif event.key == pygame.K_SPACE:
                player1.attack(player2)

    # Draw the background and player health bars
    screen.blit(background_image, background_position)
    for player in players:
        player.draw_health_bar()

    # Update and draw the players
    players.update()
    players.draw(screen)

    # Update the display and wait for the next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

