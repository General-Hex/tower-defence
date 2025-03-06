"""
Main Module for the Tower Defence Mayhem Game
Game Title: Tower Defence Mayhem
Author: Ryan Beikrasouli
Date created: 15/02/2025
Futher info: README.md
"""

# IMPORTING MODULES

try: 
    import pygame
    pygame.init()
    pygame.mixer.init()
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

try:
    from gameLoop import mainGameLoop
except ModuleNotFoundError as err:
    print(err)
    print("Error missing module please ensure all this games modules are present in their original directory")

# Main Game
if __name__ == '__main__':  
    # Pygames Setups
    clock = pygame.time.Clock()
    mainGameLoop(clock)