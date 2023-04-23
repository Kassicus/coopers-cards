import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Colors():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHTIE = pygame.Color(255, 255, 255, 255)

color = Colors()

events = None
frames = 120
delta_time = 0