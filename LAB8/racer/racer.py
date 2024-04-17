import pygame
import random

pygame.init()
# Colors
WHITE = (255, 255, 255)
# Game size
size_x = 400
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Dulat")
# Street background
back = pygame.image.load('AnimatedStreet.png')
# Objects
player = pygame.image.load('Player.png')
pl_x = 200
pl_y = 500
pl_speed = 5
# Coin
coin = pygame.image.load('coin.png')
coin_x = random.randint(1, 40) * 10
coin_y = 0
counter = 0
text_counter = pygame.font.Font('Roboto-Black.ttf', 30)
# FPS
clock = pygame.time.Clock()
game = True

while game:
    screen.blit(back, (0, 0))
    screen.blit(player, (pl_x, pl_y))
    screen.blit(coin, (coin_x, coin_y))

    # Rectangles for collision detection
    pl_rect = player.get_rect(topleft=(pl_x, pl_y))
    coin_rect = coin.get_rect(topleft=(coin_x, coin_y))

    # Rendering counter
    text = text_counter.render(f'{counter}', True, WHITE)
    screen.blit(text, (0, 0))

    # Collision detection and coin repositioning
    if pl_rect.colliderect(coin_rect):
        counter += 1
        coin_x = random.randint(1, 40) * 10
        coin_y = 0

    # Moving coin downwards and repositioning it if it reaches the bottom
    if coin_y >= size_y:
        coin_x = random.randint(1, 40) * 10
        coin_y = 0
    else:
        coin_y += 5

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pl_x > 0:
        pl_x -= pl_speed
    if keys[pygame.K_RIGHT] and pl_x < size_x - player.get_width():
        pl_x += pl_speed
    if keys[pygame.K_UP] and pl_y > 0:
        pl_y -= pl_speed
    if keys[pygame.K_DOWN] and pl_y < size_y - player.get_height():
        pl_y += pl_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
