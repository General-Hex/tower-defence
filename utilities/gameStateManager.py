from models.gameStates import MainGame, MainMenu, LevelsPage

class GameStateManager():

    def __init__(self, clock):
        self.__MainGameState = MainGame()
        self.__MainMenuState = MainMenu()
        self.__LevelsState = LevelsPage()
        self.__clock = clock

    def runGame(self):
        self.__screen = 'main menu'
        self.__loops = 0
        while "POTATO":
            if self.__screen == 'main menu':
                if self.__loops == 0:
                    self.__screen = self.__MainMenuState.enter(self.__clock, True)
                    self.__loops = 1
                else:
                    self.__screen = self.__MainMenuState.enter(self.__clock)

            elif self.__screen == 'levels':
                self.__screen = self.__LevelsState.enter(self.__clock)
        
            elif self.__screen[0] == 'main game':
                self.__screen = self.__MainGameState.enter(self.__clock, int(self.__screen[1]))
        
            
                

            


    
    