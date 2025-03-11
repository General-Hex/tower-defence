from models.gameStates import MainGame, MainMenu

class GameStateManager():

    def __init__(self, clock):
        self.__MainGameState = MainGame()
        self.__MainMenuState = MainMenu()
        self.__clock = clock

    # def runMainMenu(self):
    #     self.__MainMenuState.enter(self.__clock)

    # def runMainGame(self):
    #     self.__MainGameState.enter(self.__clock)

    def runGame(self):
        self.__screen = 'main menu'
        while "POTATO":
            if self.__screen == 'main menu':
                self.__screen = self.__MainMenuState.enter(self.__clock)

            if self.__screen == 'levels':
                self.__screen = self.__MainGameState.enter(self.__clock)
                

            


    
    