'''
Author: Ryan Beikrasouli
ID: 6137
Date created: 15/02/2025
Futher info: README
'''
# IMPORTING MODULES
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
    from enemies import Zombie, Skeleton
except ModuleNotFoundError as err:
    print(err)
    print("Error missing enemies module please ensure all this games modules are present in their original directory")
    quit()

try:
    from otherFunctions import Try_Load, addText
except ModuleNotFoundError as err:
    print(err)
    print("Error missing otherFunctions module please ensure all this games modules are present in their original directory")
    quit()

try:
    from world import World
except ModuleNotFoundError as err:
    print(err)
    print("Error missing world module please ensure all this games modules are present in their original directory")
    quit()

try:
    from turrets import Cannon, Machinelaser, createTurret, selectTurret, clearSelection
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

try:
    from buttons import Button
except ModuleNotFoundError as err:
    print(err)
    print("Error missing buttons module please ensure all this games modules are present in their original directory")
    quit()

# Checking spawn cooldown based on 2x speed
def checkCooldown(doubleSpeed:bool):
    if doubleSpeed:
        return pygame.time.get_ticks() - lastEnemySpawn >= SPAWN_COOLDOWN//2 and levelStarted
    else:
        return pygame.time.get_ticks() - lastEnemySpawn >= SPAWN_COOLDOWN and levelStarted

# Pygames Setups
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()

# Main Game Screen
SCREEN = pygame.display.set_mode([SCREEN_WIDTH + SIDE_PANNEL, SCREEN_HEIGHT])

# Game Fonts
FONT = pygame.font.SysFont('Consolas', 80, bold=True)
FONT3 = pygame.font.SysFont('Consolas', 20, bold=False)

# Game Buttons
buyCannonButton = Button(FONT3, "CANNON: $200", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 140, 205, 30, True, True)
buyMachinelaserButton = Button(FONT3, "MACHINELASER: $250", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 180, 215, 30, True, True)
startButton = Button(FONT3, "START WAVE", (255, 255, 255), (0, 255, 0), (0, 220, 0), SCREEN_WIDTH + 150, 100, 155, 30, True, True)
cancelButton =  Button(FONT3, "Cancel", (255, 255, 255), (255, 0, 0), (255, 95, 31), SCREEN_WIDTH + 150, 220, 75, 30, True, True)
upgradeButton = Button(FONT3, "Upgrade: $", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 460 , 200, 30, True, True)
restartButton = Button(FONT3, "Restart?", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH//2 + 80, SCREEN_HEIGHT//2, 200, 30, True, True)
speedButton = Button(FONT3, "2X speed", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH + 150, 500 , 200, 30, True, True)

# Game World Setup
world = World()
world.processData()
world.processEnemies()

# Sprite Groups
allEnemies = pygame.sprite.Group()
allTurrets = pygame.sprite.Group()

# Game Variables
placingTurrets = False
selectedTurret = None 
lastEnemySpawn =  pygame.time.get_ticks()

demoCannon = Cannon(0, 0)
demoMachinelaser = Machinelaser(0, 0)
levelStarted = False  
gameOver = False
gameOutcome = 0 # win: 1, loss: -1, Neither: 0 
doubleSpeed = False
turretType = None

# MAIN GAME LOOP
pygame.display.set_caption("Tower Defence Mayhem")
Try_Load('main_theme.mp3', 'music')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(loops=-1)
while "POTATO":
    # Setting FPS
    clock.tick(FPS)

    # Checking Buttons
    if cancelButton.MouseClick():
        placingTurrets = False
        
    if buyCannonButton.MouseClick():
        placingTurrets = True
        cursorTurret = Cannon(0, 0)
        turretType = "cannon"
    
    elif buyMachinelaserButton.MouseClick():
        placingTurrets = True
        cursorTurret = Machinelaser(0, 0)
        turretType = "machinelaser"
    
    if selectedTurret:
        if upgradeButton.MouseClick() and world.money >= selectedTurret.upgradeCost: 
            selectedTurret.upgrade()
            world.money -= selectedTurret.upgradeCost
    
    if startButton.MouseClick():
        levelStarted = True
    
    if speedButton.MouseClick():
        doubleSpeed = not doubleSpeed

    # Drawing World
    SCREEN.fill((0,0,0))
    world.draw(SCREEN)
    
    # Checking Game Status
    if not gameOver:

        # Checking Game Loss
        if world.health <= 0:
            pygame.mixer.music.stop()
            Try_Load('loss_theme.mp3', 'music')
            pygame.mixer.music.play(loops=-1)
            gameOver = True
            gameOutcome = -1 
        
        # Checking Game Won
        if world.wave > WAVE_COUNT + 1:
            pygame.mixer.music.stop()
            Try_Load('victory_theme.mp3', 'music')
            pygame.mixer.music.play(loops=-1)
            gameOver = True
            gameOutcome =  1 

        # Updating Objects
        allEnemies.update(world, doubleSpeed)
        allTurrets.update(allEnemies, doubleSpeed)
        if selectedTurret:
            selectedTurret.selected = True

    

    if not gameOver:
        # Drawing Turrets
        for turret in allTurrets:
            turret.draw(SCREEN) 
        # Drawing Enemies
        if checkCooldown(doubleSpeed):
            if world.spawnedEnemies < len(world.enemyList):
                enemyType = world.enemyList[world.spawnedEnemies]
                if enemyType == "zombie":
                    newEnemy = Zombie(world.waypoints)
                elif enemyType == "skeleton":
                    newEnemy = Skeleton(world.waypoints)
                allEnemies.add(newEnemy)
                world.spawnedEnemies += 1
                lastEnemySpawn = pygame.time.get_ticks()
        
        # Checking Wave Status
        if world.checkWaveFinished():
            levelStarted = False
            lastEnemySpawn = pygame.time.get_ticks()
            world.prepareNewWave()
            world.processEnemies()
            world.money += WAVE_COMPLEATION_REWARD 

        # Drawing Enemies
        allEnemies.draw(SCREEN)   

        # Displaying Game Information Texts
        addText(SCREEN, "Money: $" + str(world.money), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 100)
        addText(SCREEN, "HP: " + str(world.health), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 80)
        addText(SCREEN, "WAVE: " + str(world.wave), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 60)
        if selectedTurret:
            addText(SCREEN, "Damage: " + str(selectedTurret.damage), FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 450)
            addText(SCREEN, "Range: " + str(selectedTurret.range), FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 410)
            addText(SCREEN, "Cooldown: " + str(selectedTurret.data[selectedTurret.tier - 1].get("cooldown")) + "ms", FONT3, (255, 255, 255), SCREEN_WIDTH + 15, SCREEN_HEIGHT -370)
            addText(SCREEN, "Tier: " + str(selectedTurret.tier) + "/4", FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 330)

            if selectedTurret.tier < 4:
                damageBonus = selectedTurret.data[selectedTurret.tier].get("damage") - selectedTurret.damage
                rangeBonus = selectedTurret.data[selectedTurret.tier].get("range") - selectedTurret.range
                cooldownBonus = selectedTurret.data[selectedTurret.tier - 1].get("cooldown") - selectedTurret.data[selectedTurret.tier].get("cooldown")
                if damageBonus > 0:
                    addText(SCREEN, "+" + str(damageBonus), FONT3, (144, 238, 144),SCREEN_WIDTH + 175, SCREEN_HEIGHT - 450)
                
                if rangeBonus > 0:
                    addText(SCREEN, "+" + str(rangeBonus), FONT3, (144, 238, 144),SCREEN_WIDTH + 175, SCREEN_HEIGHT - 410)
                
                if cooldownBonus > 0:
                    addText(SCREEN, "-" + str(cooldownBonus) + "ms", FONT3, (144, 238, 144), SCREEN_WIDTH + 215, SCREEN_HEIGHT -370)
             
        if doubleSpeed:
            speedButton.MouseCheck(SCREEN, newText="1x Speed")
        else:
            speedButton.MouseCheck(SCREEN, newText="2x Speed")

        # Updating Buy Turret Buttons
        if world.money >= demoCannon.cost:
            buyCannonButton.MouseCheck(SCREEN)
        else:
            buyCannonButton.MouseCheck(SCREEN, True, (220, 220, 220))
            placingTurrets = False

        if world.money >= demoMachinelaser.cost:
            buyMachinelaserButton.MouseCheck(SCREEN)
        else:
            buyMachinelaserButton.MouseCheck(SCREEN, True, (220, 220, 220))
            placingTurrets = False

        # Updating Cancel Button
        if placingTurrets:
            cancelButton.MouseCheck(SCREEN)
        else:
            cancelButton.active = False
        
        # Updating Start Button
        if not levelStarted:
            startButton.MouseCheck(SCREEN)
        else:
            startButton.active = False

        # Updating Upgrade Button
        if selectedTurret and selectedTurret.tier < len(TURRET_DATA):
            upgradeButton.MouseCheck(SCREEN, not (world.money >= selectedTurret.upgradeCost), (200, 200, 200), "Upgrade: $" + str(selectedTurret.upgradeCost))
        else:
            upgradeButton.active = False

        # Displaying Turret on Cursor When Placing
        if placingTurrets and pygame.mouse.get_pos()[0] <= SCREEN_WIDTH:
            cursorPos = pygame.mouse.get_pos()
            SCREEN.blit(cursorTurret.originalImage, (cursorPos[0]-50, cursorPos[1]-50))

    # GAME OVER
    else:
        pygame.draw.rect(SCREEN, (0, 0, 0), (200, 200, 500, 200), border_radius=30)
        restartButton.MouseCheck(SCREEN)
        # Game Loss
        if gameOutcome == -1:
            addText(SCREEN, "GAME OVER", FONT, (255, 0, 0), SCREEN_WIDTH//2-130, SCREEN_HEIGHT//2-130)    
        
        # Game Won
        elif gameOutcome == 1:
            addText(SCREEN, "YOU WIN", FONT, (0, 200, 0), SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2-130)    

        # Restarting Game
        if restartButton.MouseClick():
            gameOver = False 
            levelStarted = False
            placingTurrets = False
            selectedTurret = None
            lastEnemySpawn = pygame.time.get_ticks()
            world = World()
            world.processData()
            world.processEnemies()
            allEnemies.empty()
            allTurrets.empty()
    
    # Event Handling
    for event in pygame.event.get():
        # Exiting Game
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            quit()

        # Adding/Selecting Turrets
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            if mousePos[0] <= SCREEN_WIDTH and mousePos[1] <= SCREEN_HEIGHT:
                selectedTurret = None 
                clearSelection(allTurrets)
                if placingTurrets:
                    allTurrets = createTurret(mousePos, allTurrets, world, turretType)
                    

                else:
                    selectedTurret = selectTurret(mousePos, allTurrets)

    
    # Updating Display
    pygame.display.flip()