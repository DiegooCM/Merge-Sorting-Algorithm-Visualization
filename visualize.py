from math import ceil
import pygame
import numpy as np

pygame.init()

screen_length = [1280, 720]
screen = pygame.display.set_mode(screen_length)
clock = pygame.time.Clock()
running = True

my_array = [4, 9, 2, 3, 8, 1, 11]

my_array = np.random.choice(range(2, 100), size=98, replace=False)
print(my_array)

light_blue = (155, 214, 243)

width_bar = screen_length[0] // len(my_array)
height_corr = screen_length[1] // max(my_array)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for item in range(len(my_array)):
        left = width_bar * item
        top = height_corr * (max(my_array) - my_array[item])

        height_r = screen_length[1] - top
        
        pygame.draw.rect(screen, light_blue, pygame.Rect(left, top, width_bar, height_r))



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()