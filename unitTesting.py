"""
Secondary module used for unit testing
"""

import pytest
try: 
    import pygame
    pygame.init()
    pygame.mixer.init()
except ModuleNotFoundError as err:
    print(err)
    print("pygame does not seem to be installed, please install it using: pip install pygame")
    quit()

try:
    from otherFunctions import Try_Load
except ModuleNotFoundError as err:
    print(err)
    print("Error missing otherFunctions module please ensure it is correctly named and in correct directory as specified in the README.md file")
    quit()

# Testing Loading Sound Effects
def test_sound():
    sound = Try_Load('laser_shot.wav', 'sound')
    assert 'pygame.mixer.Sound' in str(type(sound))

# Testing Loading Main Musics
def test_music():
    Try_Load('main_theme.mp3', 'music')
    pygame.mixer.music.play()
    assert pygame.mixer.music.get_busy()

# Testing Loading Images
def test_image():
    image = Try_Load("Zombie Assets/zombie 1.png", 'image')
    assert 'pygame.surface.Surface' in str(type(image))