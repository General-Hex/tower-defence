# IMPORTING MODULES
try: 
    import pygame
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()
import os

# Ensure Correct File Run
if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

# OTHER FUNCTIONS

# Loading Images/Music with Error Exception if File is Not Found
def Try_Load(file:str, type:str):
    # Loading Image
    if type.lower() == 'image':
        start = os.getcwd()
        if 'Project 1' not in start:
            if 'Year 12 ATAR' not in start:
                full_path = start+'/Year 12 ATAR/Project 1/sprite images/'+str(file)
            else:
                full_path = start+'/Project 1/sprite images/'+str(file)
            try:
                image = pygame.image.load(os.path.relpath(full_path, start)).convert()
            except FileNotFoundError:
                print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
                quit()
        else:
            image = pygame.image.load(os.path.relpath('sprite images/'+str(file))).convert()
        return image
    
    # Loading Music
    elif type.lower() == 'music':
        start = os.getcwd()
        if 'Project 1' not in start:
            if 'Year 12 ATAR' not in start:
                full_path = start+'/Year 12 ATAR/Project 1/Sound Assets/'+str(file)
            else:
                full_path = start+'/Project 1/Sound Assets/'+str(file)
        
            try:
                music = pygame.mixer.music.load(os.path.relpath(full_path, start))
            except FileNotFoundError:
                print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
                quit()
        else:
            music = pygame.mixer.music.load('Sound Assets/' + str(file))
        
        return music

    # Loading Sound Effect
    elif type.lower() == 'sound':
        start = os.getcwd()
        if 'Project 1' not in start:

            if 'Year 12 ATAR' not in start:
                full_path = start+'/Year 12 ATAR/Project 1/Sound Assets/'+str(file)
            else:
                full_path = start+'/Project 1/Sound Assets/'+str(file)
            try:
                sound = pygame.mixer.Sound(os.path.relpath(full_path, start))
            except FileNotFoundError:
                print("Error", file, "file not found, please ensure it is in this working directory with the correct name")
                quit()
        else:
            sound = pygame.mixer.Sound('Sound Assets/' + str(file))
        
        return sound

# Adding Text to Display
def addText(screen:pygame.Surface, text:str, font:pygame.font.Font, colour:tuple[int, int, int], x:int, y:int):
    text_image = font.render(text, True, colour)
    screen.blit(text_image, (x, y))
