import pygame

from code.Entity import Entity
from code.constants import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.nome]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_KEY_DOWN[self.nome]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_KEY_LEFT[self.nome]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.nome]

        if pressed_key[PLAYER_KEY_RIGHT[self.nome]] and self.rect.left < WIN_WIDTH-59:
            self.rect.centerx += ENTITY_SPEED[self.nome]
