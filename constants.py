# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
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
MONEY = 650
WAVE_COMPLEATION_REWARD = 500
GRASS_TILE_VALUES = [121]

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
ENEMY_COUNT = [
    { # wave 1
    "zombie":3,
    },

    { # wave 2
    "zombie":5
    },

    { # wave 3
    "skeleton":10
    },

    { # wave 4
    "skeleton":30
    },

    { # wave 5
    "zombie":10,
    "skeleton":20
    },

]
WAVE_COUNT = len(ENEMY_COUNT)
