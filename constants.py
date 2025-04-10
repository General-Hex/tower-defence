"""
Module to store constant/shared variables
"""

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

try:
    from models.buttons import Button
except ModuleNotFoundError as err:
    print(err)
    print("Error missing buttons module please ensure all this games modules are present in their original directory")
    quit()

# MAIN GAME CONSTANTS
FPS = 60
SIDE_PANNEL = 300
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
TILE_ROWS = 15
TILE_COLUMNS = 15
TILE_SIZE = 48
TURRET_ANIMATION_FRAMES = 8
ANIMATION_DELAY = 15
SPAWN_COOLDOWN = 800
BASE_HEALTH = 100
MONEY = 350
WAVE_COMPLEATION_REWARD = 500
GRASS_TILE_VALUES = [121, 268, 49]

# Turret Upgrade Data
TURRET_DATA = [
    { # Tier 1
    "range": 90, 
    "cooldown": 1500,
    "damage": 5
    },

    { # Tier 2
    "range": 110, 
    "cooldown": 1200,
    "damage": 6
    },

    { # Tier 4
    "range": 125, 
    "cooldown": 1000,
    "damage": 7
    },

    { # Tier 4
    "range": 150, 
    "cooldown": 900,
    "damage": 10
    }
]

# Wave Data
ENEMY_COUNT1 = [
    { # wave 1
    "zombie":1,
    },

    { # wave 2
    "zombie":3
    },

    { # wave 3
    "zombie":6
    },

    { # wave 4
    "zombie":8
    },

    { # wave 5
    "zombie":20
    },

]

ENEMY_COUNT2 = [
    { # wave 1
    "zombie":3,
    },

    { # wave 2
    "zombie":5,
    "skeleton":3
    },

    { # wave 3
    "skeleton":10
    },

    { # wave 4
    "skeleton":30
    },

    { # wave 5
    "zombie":30,
    "skeleton":25
    },

]

WAVE_COUNT1 = len(ENEMY_COUNT1)
WAVE_COUNT2 = len(ENEMY_COUNT1)


# Game Fonts
FONT = pygame.font.SysFont('Consolas', 80, bold=True)
FONT2 = pygame.font.SysFont('Consolas', 50, bold=True)
FONT3 = pygame.font.SysFont('Consolas', 20, bold=False)

# Main Game Screen
SCREEN = pygame.display.set_mode([SCREEN_WIDTH + SIDE_PANNEL, SCREEN_HEIGHT])

# Game Buttons
buyCannonButton:Button = Button(FONT3, "CANNON: $200", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 140, 205, 30, True, True)
buyMachinelaserButton:Button = Button(FONT3, "MACHINELASER: $250", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 180, 215, 30, True, True)
startButton:Button = Button(FONT3, "START WAVE", (255, 255, 255), (0, 255, 0), (0, 220, 0), SCREEN_WIDTH + 150, 100, 155, 30, True, True)
cancelButton:Button =  Button(FONT3, "Cancel", (255, 255, 255), (255, 0, 0), (255, 95, 31), SCREEN_WIDTH + 150, 220, 75, 30, True, True)
upgradeButton:Button = Button(FONT3, "Upgrade: $", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 460 , 200, 30, True, True)
speedButton:Button = Button(FONT3, "2X speed", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 500 , 200, 30, True, True)
