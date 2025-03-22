"""
Secondary module used for unit testing
"""

import pytest
import pygame
pygame.init()
pygame.mixer.init()

from otherFunctions import Try_Load

def test_sound():
    sound = Try_Load('laser_shot.wav', 'sound')
    assert 'pygame.mixer.Sound' in str(type(sound))

def test_music():
    Try_Load('main_theme.mp3', 'music')
    pygame.mixer.music.play()
    assert pygame.mixer.music.get_busy()

def test_image():
    image = Try_Load("Zombie Assets/zombie 1.png", 'image')
    assert 'pygame.surface.Surface' in str(type(image))



