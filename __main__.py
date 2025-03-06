"""
Game Title: Tower Defence Mayhem
Author: Ryan Beikrasouli
Date created: 15/02/2025
Futher info: README.md
"""

# IMPORTING MODULES

try: 
    import pygame
    # Pygames Setups
    clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()

except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

from gameLoop import mainGameLoop

# Main Game
if __name__ == '__main__':  
    mainGameLoop(clock)