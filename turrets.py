# IMPORTING MODULES
try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()
from pygame.locals import RLEACCEL

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

try:
    from world import World
except ModuleNotFoundError as err:
    print(err)
    print("Error missing world module please ensure all this games modules are present in their original directory")
    quit()

import math

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

class Turret(pygame.sprite.Sprite):

    def __init__(self, tileX:int, tileY:int):
        pygame.sprite.Sprite.__init__(self)
        # TURRET ATRIBUTES 

        # Turret Positon
        self.tileX = tileX
        self.tileY = tileY
        self.x = tileX * TILE_SIZE + TILE_SIZE//2
        self.y = tileY * TILE_SIZE + TILE_SIZE//2
        
        # General
        self.data = []
        self.upgradeCost = 0
        self.cost = 0 
        self.sfx = Try_Load('gun_shot.wav', 'sound')
        self.sfx.set_volume(0.1)
        self.tier = 1 
        self.range = 0
        self.cooldown = 0
        self.damage = 0
        self.__lastShot = pygame.time.get_ticks()
        self.__updateTime = pygame.time.get_ticks()
        self.selected = False 
        self.target = None  
        self.__doubleSpeed = False
        
        # Turret Image
        self.allTurretSheets = []

        self.animationImages = None 
        self.imageIndex = 0
        self.rotationAngle = 90
        self.originalImage = None 
        self.image = None
        self.rect = None
        
    def setupRange(self):
        # Turret Range Circle
        self.rangeImage = pygame.Surface((self.range * 2, self.range * 2 ))
        self.rangeImage.fill((0, 0, 0))
        self.rangeImage.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.rangeImage, (220, 220, 220), (self.range, self.range), self.range)
        self.rangeImage.set_alpha(100)
        self.rangeRect = self.rangeImage.get_rect(center=self.rect.center)

    # Updating Turret
    def update(self, allEnemiesGroup:pygame.sprite.Group, doubleSpeed:bool):
        if self.target:
            self.__updateAnimation()
        
        else:
            if pygame.time.get_ticks() - self.__lastShot > self.cooldown:
                self.__selectTarget(allEnemiesGroup)
        
        if doubleSpeed and not self.__doubleSpeed:
            self.cooldown = self.cooldown//2
            self.__doubleSpeed = True
        elif not doubleSpeed and self.__doubleSpeed:
            self.cooldown *= 2
            self.__doubleSpeed = False

    # Selecting Target
    def __selectTarget(self, allEnemiesGroup:pygame.sprite.Group):
        xDistance = 0
        yDistance = 0

        # Selecting Living Target in Range
        for enemy in allEnemiesGroup:
            if enemy.health > 0:       
                xDistance = enemy.pos[0] - self.x
                yDistance = enemy.pos[1] - self.y
                totalDistance = math.sqrt(xDistance**2 + yDistance**2)
                if totalDistance < self.range:
                    self.target = enemy 
                    self.rotationAngle = math.degrees(math.atan2(-yDistance, xDistance))
                    self.target.health -= self.damage
                    self.sfx.play()
                    break  
    
    # Loading Turret Images from Sprite Sheet
    def loadImages(self, spriteSheet:pygame.surface.Surface):
        spriteSheet.set_colorkey(RLEACCEL) 
        size = spriteSheet.get_height()
        animationImages = [] 
        for i in range(TURRET_ANIMATION_FRAMES):
            frame = spriteSheet.subsurface(i * size, 0, size, size)
            frame = pygame.transform.scale(frame, (frame.get_width()//1.5, frame.get_height()//1.5 ))
            animationImages.append(frame)

        return animationImages

    # Updating Turret Animation
    def __updateAnimation(self):
        self.originalImage = self.animationImages[self.imageIndex]

        if pygame.time.get_ticks() - self.__updateTime >= ANIMATION_DELAY:
            self.__updateTime = pygame.time.get_ticks()
            if self.imageIndex < TURRET_ANIMATION_FRAMES - 1:
                self.imageIndex += 1
            
            else:
                self.imageIndex = 0
                self.__lastShot = pygame.time.get_ticks()
                self.target = None
    
    # Upgrading Turret
    def upgrade(self):
        self.tier += 1 
        self.range = self.data[self.tier-1].get("range")
        self.cooldown = self.data[self.tier-1].get("cooldown")
        self.damage = self.data[self.tier-1].get("damage")
        self.cooldown = self.data[self.tier-1].get("cooldown") 
        self.animationImages = self.loadImages(self.allTurretSheets[self.tier - 1])
        self.originalImage = self.animationImages[self.imageIndex]
        self.rangeImage = pygame.Surface((self.range * 2, self.range * 2 ))
        self.rangeImage.fill((0, 0, 0))
        self.rangeImage.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.rangeImage, (220, 220, 220), (self.range, self.range), self.range)
        self.rangeImage.set_alpha(100)
        self.rangeRect = self.rangeImage.get_rect(center=self.rect.center) 
        
    # Drawing Turret
    def draw(self, surface:pygame.surface.Surface):
        self.image = pygame.transform.rotate(self.originalImage, self.rotationAngle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        if self.selected:
             surface.blit(self.rangeImage, self.rangeRect)
        surface.blit(self.image, self.rect)
         
class Cannon(Turret):
    def __init__(self, tileX:int, tileY:int):
        super().__init__(tileX, tileY)

        self.data = [
            { "range": 90, "cooldown": 3000, "damage": 10}, # Tier 1

            {"range": 110, "cooldown": 2600, "damage": 12}, # Tier 2

            { "range": 125, "cooldown": 2400, "damage": 14}, # Tier 3

            { "range": 125, "cooldown": 2400, "damage": 20} # Tier 4
        ]

        self.upgradeCost = 100
        self.cost = 200 
        self.sfx = Try_Load('gun_shot.wav', 'sound')
        self.sfx.set_volume(0.1)
        self.range = self.data[self.tier-1].get("range")
        self.cooldown = self.data[self.tier-1].get("cooldown")
        self.damage = self.data[self.tier-1].get("damage")

        self.allTurretSheets = []
        for i in range(4):
            turretSheet = Try_Load('/Turret Assets/cannon_tier_'+ str(i + 1) + '.png', 'image')
            self.allTurretSheets.append(turretSheet)

        self.animationImages = self.loadImages(self.allTurretSheets[self.tier - 1])
        self.originalImage = self.animationImages[self.imageIndex]
        self.image = pygame.transform.rotate(self.originalImage, self.rotationAngle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.setupRange()
        

class Machinelaser(Turret):
    def __init__(self, tileX:int, tileY:int):
        super().__init__(tileX, tileY)

        self.data = [
            { "range": 75, "cooldown": 100, "damage": 1}, # Tier 1

            {"range": 85, "cooldown": 100, "damage": 2}, # Tier 2

            { "range": 95, "cooldown": 100, "damage": 3}, # Tier 3

            { "range": 120, "cooldown": 50, "damage": 3} # Tier 4
        ]

        self.upgradeCost = 150
        self.cost = 250 
        self.sfx = Try_Load('laser_shot.wav', 'sound')
        self.sfx.set_volume(0.1)
        self.range = self.data[self.tier-1].get("range")
        self.cooldown = self.data[self.tier-1].get("cooldown")
        self.damage = self.data[self.tier-1].get("damage")

        self.allTurretSheets = []
        for i in range(4):
            turretSheet = Try_Load('/Turret Assets/machine_laser_tier_'+ str(i + 1) + '.png', 'image')
            self.allTurretSheets.append(turretSheet)

        self.animationImages = self.loadImages(self.allTurretSheets[self.tier - 1])
        self.originalImage = self.animationImages[self.imageIndex]
        self.image = pygame.transform.rotate(self.originalImage, self.rotationAngle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.setupRange()




# OTHER TURRET FUNCTIONS

# Creating New Turret
def createTurret(mousePosition:tuple[int,int], allTurretsGroup:pygame.sprite.Group, world:World, turretType:str):
    tileX = mousePosition[0] // TILE_SIZE
    tileY = mousePosition[1] // TILE_SIZE
    mouseTileNum = tileY * TILE_ROWS + tileX 
    if world.tilemap[mouseTileNum] in GRASS_TILE_VALUES:
        tileFree = True
        for turret in allTurretsGroup:
            if (tileX, tileY) == (turret.tileX, turret.tileY):
                tileFree = False
        
        if tileFree:
            if turretType == "cannon":
                newTurret = Cannon(tileX, tileY)
            elif turretType == "machinelaser":
                newTurret = Machinelaser(tileX, tileY)

            if world.money - newTurret.cost >= 0:
                allTurretsGroup.add(newTurret)
                world.money -= newTurret.cost
    
    return allTurretsGroup

# Selecting Existing Turret
def selectTurret(mousePosition:tuple[int,int], allTurretsGroup:pygame.sprite.Group):
    tileX = mousePosition[0] // TILE_SIZE
    tileY = mousePosition[1] // TILE_SIZE

    for turret in allTurretsGroup:
        if (tileX, tileY) == (turret.tileX, turret.tileY):
            return turret  

# Clearing Selected Turret
def clearSelection(allTurretsGroup:pygame.sprite.Group):
    for turret in allTurretsGroup:
        turret.selected = False  