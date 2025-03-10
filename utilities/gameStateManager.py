from models.gameStates import MainGame, MainMenu

class GameStateManager():

    def __init__(self, clock):
        self.__MainGameState = MainGame()
        self.__MainMenuState = MainMenu()
        self.__clock = clock

    def runMainGame(self):
        self.__MainGameState.enter(self.__clock)