import pygame
import random

# --- INIT SHIT --- #
pygame.init()

# --- CONSTANTS --- #
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SCREEEN_TITLE = "Coopers Cards"

BLACK = pygame.Color(0, 0, 0, 255)
WHITE = pygame.Color(255, 255, 255, 255)

# --- GLOBAL VARS --- #
delta_time = 0
frame_cap = 120

# --- CARD CLASS --- #
class Card(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(200, 300)

        self.sprite_id = random.randint(0, 999999999)

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def get_sprite_id(self):
        return self.sprite_id

    def update(self):
        self.rect.center = self.pos

# --- GAME CLASS --- #
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption(SCREEEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.deck = pygame.sprite.Group()
        self.current_card = pygame.sprite.Group()
        self.passed_cards = pygame.sprite.Group()
        self.failed_cards = pygame.sprite.Group()

        self.populate_deck()
        self.draw_card()

    def populate_deck(self):
        for c in range(10):
            c = Card(-500, -500)
            self.deck.add(c)

    def draw_card(self):
        top_card = self.deck.sprites()[0]
        top_card.pos.x, top_card.pos.y = 600, 700
        self.current_card.add(top_card)
        self.deck.remove(top_card)

    def start(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)

        self.deck.draw(self.screen)
        self.current_card.draw(self.screen)

    def update(self):
        global delta_time

        self.deck.update()
        self.current_card.update()

        pygame.display.update()
        delta_time = self.clock.tick(frame_cap) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()