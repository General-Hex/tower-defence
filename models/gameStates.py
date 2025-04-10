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

from pygame.sprite import Group
from pygame.locals import(
    K_ESCAPE, 
    KEYDOWN,
    K_p,
    RLEACCEL)

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

try:
    from models.buttons import Button
except ModuleNotFoundError as err:
    print(err)
    print("Error missing buttons module please ensure all this games modules are present in their original directory")
    quit()

from utilities.buttonUtilities import checkButtons, buttonSetup
from utilities.mainUtilities import displayGameTexts

from abc import ABC, abstractmethod
import time

class GameState(ABC):
    """
    Game State base class for different game states such as main game and menu
    """

    def __init__(self):
        """
        Game State constructor
        """
        self.active = False
    
    @property
    @abstractmethod
    def enter(self):
        """
        Method for gamestate to present itself in the main game
        """

        pass

    @property
    @abstractmethod
    def exit(self):
        """
        Method for gamestate to remove itself from the main game
        """

        pass

class MainMenu(GameState):
    """
    Main menu subclass to handle game's main menu
    """

    def __init__(self) -> None:
        """
        Main menu constructor
        """
        super().__init__()

    def enter(self, clock, setup:bool=False) -> str:
        """
        Overide method for main menu to initilise itself in the current game
        """

        logoImage = Try_Load('main_logo.png', 'image')
        logo = pygame.transform.scale_by(logoImage, 1.5)
        logoRect = logo.get_rect(center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))
        levelsButton = Button(FONT2, 'Levels', (255, 255, 255), (6, 221, 7), (4, 149, 41), SCREEN_WIDTH//2, 100, 275, 50, False, True, Try_Load('levels_button_on.png', 'image'), Try_Load('levels_button_off.png', 'image'), 1.7)
        loginButton = Button(FONT2, 'Login', (255, 255, 255), (6, 221, 7), (4, 149, 41), SCREEN_WIDTH//2, 225, 275, 50, False, True, Try_Load('login_button_on.png', 'image'), Try_Load('login_button_off.png', 'image'), 1.8)
        quitButton = Button(FONT2, 'Quit', (255, 255, 255), (255, 0, 0), (139, 0, 0), SCREEN_WIDTH//2, 332, 275, 50, False, True, Try_Load('quit_button_on.png', 'image'), Try_Load('quit_button_off.png', 'image'), 2)
        self.active = True
        self.__nextScreen = None
        

        
        if setup or True:
            pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Tower Defence Mayhem")
            Try_Load('main_theme.mp3', 'music')
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(loops=-1)

        while self.active:
            clock.tick(FPS)
            SCREEN.blit(logo, logoRect)
            levelsButton.MouseCheck(SCREEN)
            loginButton.MouseCheck(SCREEN, True, (160, 160, 160))
            quitButton.MouseCheck(SCREEN)

            # Event Handling
            for event in pygame.event.get():
                # Exiting Game
                if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            
            if levelsButton.MouseClick(True):
                self.__nextScreen = 'levels'
                self.active = False
                return self.exit()

            if quitButton.MouseClick(True):
                pygame.quit()
                quit()

            pygame.display.flip()


    def exit(self) -> str:
        """
        Overide method for main menu to remove itself from the current game
        """

        return self.__nextScreen

class MainGame(GameState):
    """
    Main game subclass to handle running the game's actual game 
    """

    def __init__(self) -> None:
        """
        Main game constructor
        """

        super().__init__()
        self.__nextScreen = None
    
    def enter(self, clock:pygame.time.Clock, level:int) -> str:
        """
        Overide method for main game to initilise itself in the current game
        """

        # Game World Setup
        world = World(level)
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

        restartButton = Button(FONT3, "Restart", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH//2 + 80, SCREEN_HEIGHT//2 - 50, 250, 30, True, True)
        mainMenuButton = Button(FONT3, "Main Menu", (255, 255, 255), (255, 68, 51), (255, 95, 31), SCREEN_WIDTH//2 + 80, SCREEN_HEIGHT//2, 250, 30, True, True)
        
        pauseImage = Try_Load('pause_button.png', 'image')
        pauseRect = pauseImage.get_rect(center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))
        pauseImage.set_colorkey((0, 0, 0), RLEACCEL)

        paused = False
        pygame.display.set_mode((SCREEN_WIDTH + SIDE_PANNEL, SCREEN_HEIGHT))

        startTime = time.time()
        finalTime = None
        # MAIN GAME LOOP
        while "POTATO":

            if paused:
                for event in pygame.event.get():
                    # Exiting Game
                    if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        paused = not paused
                
                SCREEN.blit(pauseImage, pauseRect)
                pygame.display.flip()
                continue

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
                if world.level == 1: waveCount = WAVE_COUNT1
                elif world.level == 2: waveCount = WAVE_COUNT2
                
                if world.wave > waveCount + 1:
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
                if not finalTime:
                    finalTime = int(time.time() - startTime)
                score = 1000 - finalTime
                pygame.draw.rect(SCREEN, (0, 0, 0), (200, 200, 500, 200), border_radius=30)
                restartButton.MouseCheck(SCREEN)
                mainMenuButton.MouseCheck(SCREEN)
                # Game Loss
                if gameOutcome == -1:
                    addText("GAME OVER", FONT, (255, 0, 0), SCREEN_WIDTH//2-130, SCREEN_HEIGHT//2-130)    
                
                # Game Won
                elif gameOutcome == 1:
                    addText("YOU WIN", FONT, (0, 200, 0), SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2-130)    

                addText("Score: " + str(score), FONT3, (255,255,255), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150)
                # Restarting Game
                if restartButton.MouseClick(True):
                    gameOver = False 
                    levelStarted = False
                    placingTurrets = False
                    selectedTurret = None
                    lastEnemySpawn = pygame.time.get_ticks()
                    world = World(world.level)
                    world.processData()
                    world.processEnemies()
                    allEnemies.empty()
                    allTurrets.empty()
                
                if mainMenuButton.MouseClick(True):
                    self.__nextScreen = 'main menu'
                    return self.exit()
            
            # Event Handling
            for event in pygame.event.get():
                # Exiting Game
                if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = not paused

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

    def exit(self) -> str:
        """
        Overide method for main game to remove itself from the current game
        """

        return self.__nextScreen

class LevelsPage(GameState):
    """
    Levels Page subclass to handle the levels page of the game
    """
    def __init__(self) -> None: 
        """
        Levels Page constructor
        """
        super().__init__()
    
    def enter(self, clock:pygame.time.Clock) -> str | list:
        """
        Overide method for levels page to initilise itself in the current game
        """

        self.active = True
        levelOneButton = Button(FONT2, 'Level 1', (255, 255, 255), (255, 255, 0), (244, 187, 68), SCREEN_WIDTH//2, 100, 275, 50, False, True, Try_Load('levels_button_on.png', 'image'), Try_Load('levels_button_off.png', 'image'), 1.7)
        levelTwoButton = Button(FONT2, 'Level 2', (255, 255, 255), (255, 255, 0), (244, 187, 68), SCREEN_WIDTH//2, 225, 275, 50, False, True, Try_Load('levels_button_on.png', 'image'), Try_Load('levels_button_off.png', 'image'), 1.7)
        backButton = Button(FONT2, 'Back', (255, 255, 255), (255, 0, 0), (240, 0, 0), SCREEN_WIDTH//2, 332, 275, 50, False, True, Try_Load('quit_button_on.png', 'image'), Try_Load('quit_button_off.png', 'image'), 2)
        logoImage = Try_Load('main_logo.png', 'image')
        logo = pygame.transform.scale_by(logoImage, 1.5)
        logoRect = logo.get_rect(center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))


        while self.active:
            clock.tick(FPS)
            SCREEN.blit(logo, logoRect)
            levelOneButton.MouseCheck(SCREEN)
            levelTwoButton.MouseCheck(SCREEN)
            backButton.MouseCheck(SCREEN)

            for event in pygame.event.get():
                # Exiting Game
                if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            
            if backButton.MouseClick(True):
                self.__nextScreen = 'main menu'
                self.active = False
                return self.exit()
            
            if levelOneButton.MouseClick(True):
                self.__nextScreen = ['main game', '1']
                self.active = False
                return self.exit()

            if levelTwoButton.MouseClick(True):
                self.__nextScreen = ['main game', '2']
                self.active = False
                return self.exit()
            
            pygame.display.flip()

    
    def exit(self) -> str | list:
        return self.__nextScreen
        


    
    