"""
Module to handle the enemy classes
"""

# IMPORTING MODULES
try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()
from pygame.locals import RLEACCEL
from pygame.math import Vector2

try:
    from constants import *
except ModuleNotFoundError as err:
    print(err)
    print("Error missing constants module please ensure all this games modules are present in their original directory")
    quit()

try:
    from otherFunctions import Try_Load
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

import math

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run main.py")
    quit()

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    """
    Base enemy base class
    """

    def __init__(self, movementWaypoints:list) -> None:
        """
        Enemy constructor
        """

        pygame.sprite.Sprite.__init__(self)
        # ENEMY ATRIBUTES 
        # General
        self.health = 0
        self.worth =  0
        self.damage = 0
        self.movementSpeed = 0
        self.__speedDoubled = False
         
        # Waypoint Movement
        self.__waypoints = movementWaypoints
        self.pos = Vector2(self.__waypoints[0])
        self.__nextWaypointIndex = 1
        
        # Image
        self.loops = 0
        self.__rotationAngle = 0
        self.imageIndex = 1
        self.originalImage = Try_Load("Zombie Assets/zombie 1.png", 'image') # default enemy image is a zombie
        self.originalImage.set_colorkey((0, 0, 0), RLEACCEL)
        self.originalImage = pygame.transform.scale(self.originalImage,(self.originalImage.get_width()//5, self.originalImage.get_height()//5))
        self.image = pygame.transform.rotate(self.originalImage, self.__rotationAngle)
        
        # Positioning
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    # Enemy Update
    def update(self, world:World, doubleSpeed:bool) -> None:
        """
        Method to update enemy animation and movement
        """

        if doubleSpeed and not self.__speedDoubled:
            self.movementSpeed *= 2
            self.__speedDoubled = True
        elif not doubleSpeed and self.__speedDoubled:
            self.movementSpeed = self.movementSpeed/2
            self.__speedDoubled = False

        self.__speedDoubled = doubleSpeed
        self.animate()
        self.__move(world)
        self.__updateRotation()
        self.__checkAlive(world)
        self.loops += 1
    
    # Move Enemy
    def __move(self, world:World) -> None:
        """
        Method to move enemy to next waypoint
        """

        if self.__nextWaypointIndex <= len(self.__waypoints) - 1:
            self.target = Vector2(self.__waypoints[self.__nextWaypointIndex])
            self.__movement = self.target - self.pos
        
        else:
            self.kill()
            world.health -= self.damage
            world.missedEnemies += 1 
        
        self.target_distance = self.__movement.length()
        if self.target_distance >= self.movementSpeed:
            self.pos += self.__movement.normalize() * self.movementSpeed
        else:
            if self.target_distance != 0:
                self.pos += self.__movement.normalize() * self.target_distance
            
            self.__nextWaypointIndex += 1
            
            
        self.rect.center = self.pos

# Animating Enemy
    def animate(self) -> None:
        """
        Method to animate the enemy sprite
        """

        if self.imageIndex + 1 > 6:
            self.imageIndex = 1
        
        if self.loops % 10 == 0:
            self.imageIndex += 1
        
        self.originalImage = Try_Load("Default Assets/default_sprite " + str(self.imageIndex) + ".png", 'image')
        self.originalImage.set_colorkey((0, 0, 0), RLEACCEL)
        self.originalImage = pygame.transform.scale(self.originalImage,(self.originalImage.get_width()//3, self.originalImage.get_height()//3))

    # Rotating Enemy Image
    def __updateRotation(self) -> None:
        """
        Method to update rotation of enemy sprite
        """

        distance = self.target - self.pos
        self.__rotationAngle = math.degrees(math.atan2(-distance[1], distance[0]))
        rotateX = int(self.__rotationAngle) < -175 or int(self.__rotationAngle) > 175
        
        self.image = self.image = pygame.transform.flip(self.originalImage, rotateX, False)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    # Checking Health Status
    def __checkAlive(self, world:World) -> None:
        """
        Method to check if enemy is still alive
        """

        if self.health <= 0:
            world.money += self.worth
            world.killedEnemies += 1
            self.kill()


class Zombie(Enemy):
    """
    Zombie enemy subclass
    """

    def __init__(self, movementWaypoints:list) -> None:
        """
        Zombie constructor
        """

        super().__init__(movementWaypoints)
        self.health = 20
        self.movementSpeed = 1
        self.worth = 10
        self.damage = 10
        self.originalImage = Try_Load("Zombie Assets/zombie 1.png", 'image')
    
    # Animating Enemy
    def animate(self) -> None:
        """
        Overiding method to animate zombie sprite
        """

        if self.imageIndex + 1 > 8:
            self.imageIndex = 1
        
        if self.loops % 10 == 0:
            self.imageIndex += 1
        
        self.originalImage = Try_Load("Zombie Assets/zombie " + str(self.imageIndex) + ".png", 'image')
        self.originalImage.set_colorkey((0, 0, 0), RLEACCEL)
        self.originalImage = pygame.transform.scale(self.originalImage,(self.originalImage.get_width()//5, self.originalImage.get_height()//5))

class Skeleton(Enemy):
    """
    Skeleton enemy subclass
    """

    def __init__(self, movementWaypoints:list) -> None:
        """
        Skeleton constructor
        """

        super().__init__(movementWaypoints)
        self.health = 5
        self.movementSpeed = 5
        self.worth = 5
        self.damage = 5
        self.originalImage = Try_Load("Skeleton Assets/skeleton 1.png", 'image')
    
    # Animating Enemy
    def animate(self) -> None:
        """
        Overiding method to animate skeleton sprite
        """
        
        if self.imageIndex + 1 > 4:
            self.imageIndex = 1
        
        if self.loops % 10 == 0:
            self.imageIndex += 1
        
        self.originalImage = Try_Load("Skeleton Assets/skeleton " + str(self.imageIndex) + ".png", 'image')
        self.originalImage.set_colorkey((0, 0, 0), RLEACCEL)
        self.originalImage = pygame.transform.scale(self.originalImage,(self.originalImage.get_width()//1.5, self.originalImage.get_height()//1.5))