import pygame
import numpy as np
from time import sleep

import merge as merge
import visualize


def main():
    #Array creation and solution
    array = [10,9,8,7,6,5,4,3,2,1]
    #array = np.random.choice(range(2, 100), size=50, replace=False)
    result, lista_animacion = merge.merge_sort(array)
    arrays = merge.animation_arrays(lista_animacion[:-1], array)
    arr_idx = 0

    #Animation visualization
    
    running = True
    display = visualize.display()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        if arr_idx < len(arrays):
            display.draw(arrays[arr_idx])
            sleep(0.3)
            arr_idx += 1
        else:
            display.draw(result)
            sleep(3)
            running = False


    pygame.quit()

if __name__ == '__main__':
    main()
    
    
    


'''import time
time.perf_counter()
32311.48899951

time.perf_counter()  # A few seconds later
32315.261320793'''