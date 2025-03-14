"""
Button module to handle the button class
"""

# IMPORTING MODULES
try: 
    import pygame
    from pygame import RLEACCEL
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

# BUTTON CLASS
class Button(pygame.sprite.Sprite):
    """
    Main button class for easy creation of functional buttons in the main game
    """

    def __init__(self, font:pygame.font.Font, text:str, textColour:tuple[int, int, int], onColour:tuple[int, int, int], offColour:tuple[int, int], x:int, y:int, width:int, height:int, square:bool, singleClick:bool, onImage:pygame.surface.Surface|None=None, offImage:pygame.surface.Surface|None=None, scaleFactor:float|int|None=None) -> None:
        """
        Constructor for button class
        """
    
        pygame.sprite.Sprite.__init__(self)
        # BUTTON ATTRIBUTES
        self.__x = x 
        self.__y = y 
        self.__height = height
        self.__width = width
        self.__squareCheck = square
        self.__font = font
        self.__clicked = False
        self.__singleClick = singleClick
        self.__textColour = textColour
        self.__rawText = text
        self.active = False
        
        self.__onButtonImage = onImage
        self.__offButtonImage = offImage

        if self.__onButtonImage:
            self.__onButtonImage = pygame.transform.scale(self.__onButtonImage, (self.__onButtonImage.get_width()//scaleFactor, self.__onButtonImage.get_height()//scaleFactor))
            self.__onButtonImage.set_colorkey((0, 0, 0), RLEACCEL)

        if self.__offButtonImage:
            self.__offButtonImage = pygame.transform.scale(self.__offButtonImage, (self.__offButtonImage.get_width()//scaleFactor, self.__offButtonImage.get_height()//scaleFactor))
            self.__offButtonImage.set_colorkey((0, 0, 0), RLEACCEL)

        if self.__squareCheck:
            self.__square = pygame.Rect(x-self.__width//2, y-self.__height//2, width, height) 
            self.__squareOnColour = onColour
            self.__squareOffColour = offColour
            self.__text = font.render(str(text), textColour, textColour)
            self.__textRect = self.__text.get_rect(center=(self.__x, self.__y))
        
        else:
            self.__textOn = font.render(str(text), onColour, onColour)
            self.__textOff = font.render(str(text), offColour, offColour)
            self.__textRect = self.__textOn.get_rect(center=(self.__x, self.__y))
            self.__square = None

    # Check If Mouse On Button
    def MouseCheck(self, SCREEN, disabled:bool=False, disabledColour:tuple[int, int, int]=None, newText:str=None) -> None:
        """
        Method to draw button on game screen and react to mouse hovering
        """

        self.active = True
        if newText:
            self.__text = self.__font.render(str(newText), self.__textColour, self.__textColour)
            self.__textRect = self.__text.get_rect(center=(self.__x, self.__y))

        if pygame.mouse.get_pos()[0] in range(self.__x-self.__width//2, self.__x+self.__width//2) and pygame.mouse.get_pos()[1] in range(self.__y-self.__height//2, self.__y+self.__height//2) and not disabled:
            if self.__onButtonImage:
                SCREEN.blit(self.__onButtonImage , (self.__textRect[0] - 50, self.__textRect[1] - 25))
            
            if self.__squareCheck:
                pygame.draw.rect(SCREEN, self.__squareOnColour, self.__square)
                SCREEN.blit(self.__text, self.__textRect)
                    
            else:
                SCREEN.blit(self.__textOn, self.__textRect)
                   
        elif disabled:
            if self.__offButtonImage:
                SCREEN.blit(self.__offButtonImage, (self.__textRect[0] - 50, self.__textRect[1] - 25))

            if self.__squareCheck:
                pygame.draw.rect(SCREEN, disabledColour, self.__square)
                SCREEN.blit(self.__text, self.__textRect)
            
            else:
                SCREEN.blit(self.__font.render(self.__rawText, disabledColour, disabledColour), self.__textRect)

        else:
            if self.__offButtonImage:
                SCREEN.blit(self.__offButtonImage , (self.__textRect[0] - 50, self.__textRect[1] - 25))

            if self.__squareCheck:
                pygame.draw.rect(SCREEN, self.__squareOffColour, self.__square)
                SCREEN.blit(self.__text, self.__textRect)

            else:
                SCREEN.blit(self.__textOff, self.__textRect)
            
    # Check If Button Is Clicked
    def MouseClick(self) -> bool:
        """
        Method to check if button has been clicked
        """

        if not pygame.mouse.get_pressed()[0]:
            self.__clicked = False
        
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] in range(self.__x-self.__width//2, self.__x+self.__width//2) and pygame.mouse.get_pos()[1] in range(self.__y-self.__height//2, self.__y+self.__height//2) and not self.__clicked and self.active:
            if self.__singleClick:
                self.__clicked = True
            return True
        else:
            return False