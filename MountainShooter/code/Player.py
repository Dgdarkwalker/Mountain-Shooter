import pygame

from code.Entity import Entity
from code.constants import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.nome]
        if pressed_key[pygame.K_RIGHT] and self.rect.left < WIN_WIDTH-59:
            self.rect.centerx += ENTITY_SPEED[self.nome]
