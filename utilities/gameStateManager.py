from models.gameStates import MainGame, MainMenu, LevelsPage

class GameStateManager():

    def __init__(self, clock):
        """
        GameStateManeger Constructor
        """

        # Game State Manager Attributes
        self.__MainGameState = MainGame()
        self.__MainMenuState = MainMenu()
        self.__LevelsState = LevelsPage()
        self.__clock = clock

    def runGame(self):
        """
        Game State Manager Method to Handle Running Game and Different Game States
        """
        self.__screen = 'main menu'
        self.__loops = 0

        # Inifinite Game Loop
        while "POTATO":

            # Starting Main Menu Screen
            if self.__screen == 'main menu':
                if self.__loops == 0:
                    self.__screen = self.__MainMenuState.enter(self.__clock, True)
                    self.__loops = 1
                else:
                    self.__screen = self.__MainMenuState.enter(self.__clock)

            # Starting Level Selection Screen
            elif self.__screen == 'levels':
                self.__screen = self.__LevelsState.enter(self.__clock)
            
            # Starting Main Game With Level Selected
            elif self.__screen[0] == 'main game':
                self.__screen = self.__MainGameState.enter(self.__clock, int(self.__screen[1]))
        
            
                

            


    
    