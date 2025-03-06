"""
Module to handle generic functions such as loading sounds/images with error exception and adding text to game
"""

# IMPORTING MODULES
try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

from constants import SCREEN, SPAWN_COOLDOWN
import os

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

# OTHER FUNCTIONS

# Loading Images/Music with Error Exception if File is Not Found
def Try_Load(file:str, type:str) -> pygame.surface.Surface|pygame.mixer.Sound|None:
    """
    Function which imports images/music/sound with error exception
    """
    
    # Loading Image
    if type.lower() == 'image':
        try: 
            image = pygame.image.load(os.path.relpath('sprite images/'+str(file))).convert()
        except FileNotFoundError:
            print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
            quit()
        return image
    
    # Loading Music
    elif type.lower() == 'music':
        try:
            pygame.mixer.music.load('Sound Assets/' + str(file))
        except FileNotFoundError:
            print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
            quit()
        
        return

    # Loading Sound Effect
    elif type.lower() == 'sound':
        try:
            sound = pygame.mixer.Sound('Sound Assets/' + str(file))
        except FileNotFoundError:
            print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
            quit()
        return sound

# Adding Text to Display
def addText(text:str, font:pygame.font.Font, colour:tuple[int, int, int], x:int, y:int):
    """
    Function to add text to main game screen
    """

    text_image = font.render(text, True, colour)
    SCREEN.blit(text_image, (x, y))

# Checking Spawn Cooldown Based on 2x Speed
def checkCooldown(doubleSpeed:bool, lastEnemySpawn:int, levelStarted:bool) -> bool:
    """
    Function to check if the cooldown time for enemy spawning has passed
    """
    
    if doubleSpeed:
        return pygame.time.get_ticks() - lastEnemySpawn >= SPAWN_COOLDOWN//2 and levelStarted
    else:
        return pygame.time.get_ticks() - lastEnemySpawn >= SPAWN_COOLDOWN and levelStarted
