import pygame

from sys import exit
from time import sleep

pygame.init()

# screen = pygame.display.set_mode((W, H))
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# test_font=pygame.font.Font(type,size)
test_font = pygame.font.Font("font/Symtext.ttf", 30)

sky_surface = pygame.image.load("graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

# text_surface = test_font.render(Text,AA,Colour)
text_surface = test_font.render("My game", True, (255, 0, 0))

# Score:
score = 0
score_surface = test_font.render(f"Score:{score} ", True, (64, 64, 64))

# Displaying an enemy

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# Constants:
snail_x_pos = 750
snail_y_pos = 300
snail_speed = 3
player_speed = 3
player_x_pos = 80
player_y_pos = 300
player_gravity = 0

# Player:

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()

# Creating rectangles for collision purposes:

# Creating rectangle for player:
player_rect = player_surface.get_rect(midbottom=(player_x_pos, player_y_pos))

# Creating rectangle for snail:

snail_rect = snail_surface.get_rect(midbottom=(snail_x_pos, snail_y_pos))

# Creating rectangle for score:

score_rect = score_surface.get_rect(midright=(800, 30))

# Creating rectangle for title:

text_rect = text_surface.get_rect(center=(400, 20))

"""
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""
# THE MAIN LOOP:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("Collision")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                print("jump")
            if event.key == pygame.K_DOWN:
                print("Down")

    # Gravity for the player:
    player_gravity += 0.981
    player_rect.y += player_gravity

    # displaying different surfaces and bodies on the screen(sky,ground,etc):

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # Displaying a rectangle to surround the score:
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_surface, score_rect)
    screen.blit(text_surface, text_rect)

    # A condition to set the enemy back when it exits the screen
    if snail_rect.right <= 0:
        snail_rect.right = 850
    if player_rect.left >= 800:
        player_rect.right = 0

    if player_rect.colliderect(snail_rect):
        score += 1

    # Moving the characters at a certain speed (e.g: 1 pixel at a time)
    screen.blit(player_surface, player_rect)
    player_rect.right += player_speed
    screen.blit(snail_surface, snail_rect)
    snail_rect.right -= snail_speed

    # Keyboard inputs:

    # keys=(pygame.key.get_pressed())

    # if keys[pygame.K_UP]or keys[pygame.K_SPACE]:
    #     print("jump")
    # if keys[pygame.K_DOWN] :
    #     print("down")
    # if keys[pygame.K_RIGHT]:
    #     print("speed up")
    # if keys[pygame.K_LEFT]:
    #     print("slow down")

    # Getting the mouse position:
    mouse_pos = pygame.mouse.get_pos()

    # condition for collisions:
    # if player_rect.colliderect(snail_rect):
    # print("collision")

    # else:
    # print("no collision")

    # draw all of our elements
    # Update everything
    pygame.display.update()
    # Setting the highest frame rate:
    clock.tick(60)
