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

class CardGroup():
    def __init__(self, x: int, y: int):
        self.pos = pygame.math.Vector2(x, y)

        self.cards = pygame.sprite.Group()

    def add_to_group(self, card: pygame.sprite.Sprite):
        card.pos = self.pos
        self.cards.add(card)

    def remove_from_group(self, card: pygame.sprite.Sprite):
        self.cards.remove(card)

    def draw(self, surface: pygame.Surface):
        self.cards.draw(surface)

    def update(self):
        self.cards.update()