"""
Module to handle the world class
"""

# IMPORTING MODULES
import json
import random

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

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

# WORLD CLASS
class World():
    """
    World class to control game events and information such as the map and enemy spawn data
    """

    def __init__(self, level:int) -> None:
        """
        Constructor for world class
        """

        # WORLD ATTRIBUTES
        self.wave = 1 
        self.health = BASE_HEALTH
        self.money = MONEY
        self.enemyList = []
        self.waypoints = []
        self.tilemap = [] 
        self.spawnedEnemies =  0 
        self.killedEnemies = 0
        self.missedEnemies = 0
        self.level = level

        if level == 1:
            with open('sprite images/map1.json') as file:
                self.__worldData = json.load(file)
            self.__image = Try_Load('map1.png', 'image')
            self.y_offset = 70
        
        elif level == 2:
            with open('sprite images/map2.json') as file:
                self.__worldData = json.load(file)
            self.__image = Try_Load('map2.png', 'image')
            self.y_offset = 250

    # Prossesing Data From .json File
    def processData(self) -> None:
        """
        Method to process raw data from .json file
        """

        for layer in self.__worldData["layers"]:
            if layer["name"] == "tilemap":
                 self.tilemap = layer["data"]
            elif layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypointData = obj["polyline"]
                    self.__processWaypoints(waypointData)

    
    # Processing Waypoints from Data
    def __processWaypoints(self, data:dict) -> None:
        """
        Method to extract and process waypoints from data
        """

        for point in data:
            x_coordinant = point.get("x")
            y_coordinant = point.get("y") + self.y_offset
            self.waypoints.append((x_coordinant, y_coordinant))

    # Processing Enemy Spawning
    def processEnemies(self) -> None:
        """
        Method to handle the spawning of enemies in waves
        """
        if self.level == 1:
            if self.wave < WAVE_COUNT1 + 1:
                enemies = ENEMY_COUNT1[self.wave -1]

                for enemy_type in enemies:
                    enemies_to_spawn = enemies[enemy_type]
                    for i in range(enemies_to_spawn):
                        self.enemyList.append(enemy_type)
        
        elif self.level == 2:
            if self.wave < WAVE_COUNT2 + 1:
                enemies = ENEMY_COUNT2[self.wave -1]

                for enemy_type in enemies:
                    enemies_to_spawn = enemies[enemy_type]
                    for i in range(enemies_to_spawn):
                        self.enemyList.append(enemy_type)

        random.shuffle(self.enemyList)

    # Checking Wave Compleation
    def checkWaveFinished(self) -> bool:
        """
        Method to check if the current enemy wave has finished
        """

        return self.killedEnemies + self.missedEnemies == len(self.enemyList)
    
    # Preparing for New Wave
    def prepareNewWave(self) -> None:
        """
        Method to prepare the next enemy wave
        """

        self.enemyList = []
        self.spawnedEnemies = 0
        self.killedEnemies = 0
        self.missedEnemies = 0
        self.wave += 1

    # Draw World
    def draw(self) -> None:
        """
        Method to draw map on main game screen
        """
        
        SCREEN.blit(self.__image, (0, 0))

    