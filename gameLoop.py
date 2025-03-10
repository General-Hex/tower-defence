"""
Module which handles main game loop including event handling
"""

if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

from pygame.sprite import Group
from pygame.locals import(
    K_ESCAPE, 
    KEYDOWN)

try:
    from models.enemies import Zombie, Skeleton
except ModuleNotFoundError as err:
    print(err)
    print("Error missing enemies module please ensure all this games modules are present in their original directory")
    quit()

try:
    from otherFunctions import Try_Load, addText, checkCooldown
except ModuleNotFoundError as err:
    print(err)
    print("Error missing otherFunctions module please ensure all this games modules are present in their original directory")
    quit()

try:
    from models.world import World
except ModuleNotFoundError as err:
    print(err)
    print("Error missing world module please ensure all this games modules are present in their original directory")
    quit()

try:
    from models.turrets import Cannon, Machinelaser, createTurret, selectTurret, clearSelection
except ModuleNotFoundError as err:
    print(err)
    print("Error missing turrets module please ensure all this games modules are present in their original directory")
    quit() 

try:
    from constants import *
except ModuleNotFoundError as err:
    print(err)
    print("Error missing constants module please ensure all this games modules are present in their original directory")
    quit()

from utilities.buttonUtilities import checkButtons, buttonSetup
from utilities.mainUtilities import displayGameTexts

def mainGameLoop(clock:pygame.time.Clock):
    """
    Main game loop function which initialises the game instance and handles events
    """

    