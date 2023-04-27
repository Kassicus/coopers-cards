import pygame

import lib

class Card(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = pygame.math.Vector2(-500, -500)
        self.size = pygame.math.Vector2(150, 250)

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pass
