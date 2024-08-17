from math import ceil

import pygame
import numpy as np

screen_length = [1280, 720]
screen = pygame.display.set_mode(screen_length)

light_green = (0, 255, 110)
light_grey = (190, 190, 190)
red = (255, 0, 0)


class display():
    def __init__(self):
        pass

    def draw(self, arr, cols):
        '''Draws the array given'''
        screen.fill("black")

        width_bar = screen_length[0] // len(arr)
        height_corr = screen_length[1] // max(arr)

        for item in range(len(arr)):
            # The color default is grey, but if is completed (cols = None) the color turns green, 
            # Also some columns are in red, to see where the algorithm has been sorting.
            color = light_grey
            if cols == None:
                color = light_green
            elif item in cols:
                color = red

            left = width_bar * item
            top = height_corr * (max(arr) - arr[item])

            height_r = screen_length[1] - top
            
            pygame.draw.rect(screen, color, pygame.Rect(left, top, width_bar, height_r))
            
        
        
        pygame.display.flip()
            
