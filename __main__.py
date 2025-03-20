"""
Main Module for the Tower Defence Mayhem Game
Game Title: Tower Defence Mayhem
Author: Ryan Beikrasouli
Date created: 15/02/2025
Futher info: README.md
"""

# IMPORTING MODULES


import pygame
pygame.init()
pygame.mixer.init()


from utilities.gameStateManager import GameStateManager

# Main Game
if __name__ == '__main__':  
    # Pygames Setups
    clock = pygame.time.Clock()
    gameStateManager = GameStateManager(clock)

    gameStateManager.runGame()