from math import ceil

import pygame
import numpy as np



screen_length = [1280, 720]
screen = pygame.display.set_mode(screen_length)

light_blue = (155, 214, 243)

class display():
    def __init__(self):
        pass

    def draw(self, arr):
        screen.fill("black")

        width_bar = screen_length[0] // len(arr)
        height_corr = screen_length[1] // max(arr)

        for item in range(len(arr)):
            left = width_bar * item
            top = height_corr * (max(arr) - arr[item])

            height_r = screen_length[1] - top
            
            pygame.draw.rect(screen, light_blue, pygame.Rect(left, top, width_bar, height_r))
        
        
        pygame.display.flip()
            
