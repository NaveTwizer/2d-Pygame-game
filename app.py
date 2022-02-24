from colors import Colors
from core import Rectangle, initialize, play_music_repeat, update_screen

import pygame

initialize()

#setup needed variables and settings
background_color = (0,255,255)
(width, height) = (800, 800)
TITLE = "Shooter game"
bg_img = pygame.image.load(r"images\background.jpeg")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)
#player position
player_left = 100
player_top = 50
player_width = 65
player_height = 65
#player boundaries
player_x_boundry1 = 790
player_y_boundry1 = 0
player_x_boundry2 = 0
player_y_boundry2 = 790
#player speed
speed = 7
playlist = [r"music\background1.wav"]
play_music_repeat(playlist[0])

running = True
while running:
    update_screen()

    R1 = Rectangle(screen, Colors.NAVY, player_left, player_top, player_width, player_height)
    screen.blit(bg_img, (0,0))
    R1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_top -= speed
            elif event.key == pygame.K_a:
                player_left -= speed
            elif event.key == pygame.K_d:
                player_left += speed
            elif event.key == pygame.K_s:
                player_top += speed
            if (player_left > player_x_boundry1):
                player_left = 0
            elif (player_left < player_x_boundry2):
                player_left = 755
            elif (player_top < player_y_boundry1):
                player_top = 755
            elif (player_top > player_y_boundry2):
                player_top = 6
    
    update_screen()
