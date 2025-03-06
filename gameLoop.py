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
    from otherFunctions import Try_Load, addText, checkCooldown
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

from utilities.buttonUtilities import checkButtons, buttonSetup
from utilities.mainUtilities import displayGameTexts

def mainGameLoop(clock:pygame.time.Clock):
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
    cursorTurret = None

    # MAIN GAME LOOP
    pygame.display.set_caption("Tower Defence Mayhem")
    Try_Load('main_theme.mp3', 'music')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(loops=-1)

    while "POTATO":
        # Setting FPS
        clock.tick(FPS)

        # Updating Buttons
        buttonData = checkButtons(world, cursorTurret, selectedTurret, placingTurrets, levelStarted, doubleSpeed, turretType)

        placingTurrets = buttonData[0]
        cursorTurret = buttonData[1]
        turretType = buttonData[2]
        levelStarted = buttonData[3]
        doubleSpeed = buttonData[4]

        # Drawing World
        SCREEN.fill((0,0,0))
        world.draw()
        
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

            # Drawing Turrets
            for turret in allTurrets:
                turret.draw(SCREEN) 

            # Drawing Enemies
            if checkCooldown(doubleSpeed, lastEnemySpawn, levelStarted):
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
            
            # Displaying Game Text
            displayGameTexts(world, selectedTurret)
            
            # Drawing Buttons
            placingTurrets = buttonSetup(doubleSpeed, levelStarted, placingTurrets, world, demoCannon, demoMachinelaser, turretType, selectedTurret)

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
                addText("GAME OVER", FONT, (255, 0, 0), SCREEN_WIDTH//2-130, SCREEN_HEIGHT//2-130)    
            
            # Game Won
            elif gameOutcome == 1:
                addText("YOU WIN", FONT, (0, 200, 0), SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2-130)    

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