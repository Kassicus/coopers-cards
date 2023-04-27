import pygame

import lib
import cards

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption("Coopers Cards")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        test = cards.Card()

        self.todo_cards = pygame.sprite.Group()
        self.current_card = pygame.sprite.Group()
        self.passed_cards = pygame.sprite.Group()
        self.failed_cards = pygame.sprite.Group()
        
        self.todo_cards.add(test)

    def move_card(self, card, group):
        pass #TODO This needs to change to card groups, they need more info than just sprite groups.

    def start(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        self.screen.fill(lib.color.BLACK)

        self.todo_cards.draw(self.screen)

    def update(self):
        self.todo_cards.update()

        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.frames) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()