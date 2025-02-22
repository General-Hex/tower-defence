# IMPORTING MODULES
import json

try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

try:
    from otherFunctions import Try_Load
except ModuleNotFoundError as err:
    print(err)
    print("Error missing otherFunctions module please ensure all this games modules are present in their original directory")
    quit()

try:
    from constants import *
except ModuleNotFoundError as err:
    print(err)
    print("Error missing constants module please ensure all this games modules are present in their original directory")
    quit()
import random

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

# WORLD CLASS
class World():
    def __init__(self):
        # WORLD ATTRIBUTES
        self.wave = 1 
        self.health = BASE_HEALTH
        self.money = MONEY
        self.enemyList = []
        
        #with open('Year 12 ATAR/Project 1/sprite images/map1.json') as file:
        with open('sprite images/map1.json') as file:
            self.__worldData = json.load(file)
        self.__image = Try_Load('map1.png', 'image')
        self.waypoints = []
        self.tilemap = [] 
        self.spawnedEnemies =  0 
        self.killedEnemies = 0
        self.missedEnemies = 0

    # Prossesing Data From .json File
    def processData(self):
        for layer in self.__worldData["layers"]:
            if layer["name"] == "tilemap":
                 self.tilemap = layer["data"]
            elif layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypointData = obj["polyline"]
                    self.__processWaypoints(waypointData)

    
    # Processing Waypoints from Data
    def __processWaypoints(self, data:dict):
        for point in data:
            x_coordinant = point.get("x")
            y_coordinant = point.get("y") + 70
            self.waypoints.append((x_coordinant, y_coordinant))

    # Processing Enemy Spawning
    def processEnemies(self):
        if self.wave < WAVE_COUNT + 1:
            enemies = ENEMY_COUNT[self.wave -1]

            for enemy_type in enemies:
                enemies_to_spawn = enemies[enemy_type]
                for i in range(enemies_to_spawn):
                    self.enemyList.append(enemy_type)

        random.shuffle(self.enemyList)

    # Checking Wave Compleation
    def checkWaveFinished(self):
        return self.killedEnemies + self.missedEnemies == len(self.enemyList)
    
    # Preparing for New Wave
    def prepareNewWave(self):
        self.enemyList = []
        self.spawnedEnemies = 0
        self.killedEnemies = 0
        self.missedEnemies = 0
        self.wave += 1

    # Draw World
    def draw(self, surface:pygame.surface.Surface):
        surface.blit(self.__image, (0, 0))

    