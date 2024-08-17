import pygame
import numpy as np
from time import sleep

import merge
import visualize

def main():
    
    #Array creation and solution
    size = 160
    arr = np.random.choice(range(1, 200), size=size, replace=False)
    result, lista_animacion = merge.merge_sort(arr)
    arrays = merge.animation_arrays(lista_animacion[:-1], arr)

    #Animation visualization
    running = True
    display = visualize.display()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        try:
            display.draw(next(arrays), next(arrays)) #Draws the array of 'arrays'
        except StopIteration:
            # When there are no more arrays to display, it displays the sorted array
            display.draw(result, None)
            sleep(3) #A bit of delay to see the sorted array
            running = False


        sleep(size * 0.0003) #A bit of delay for being able to see the animation

    pygame.quit()

if __name__ == '__main__':
    main()