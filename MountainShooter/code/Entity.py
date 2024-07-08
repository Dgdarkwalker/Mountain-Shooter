from abc import ABC, abstractmethod

import pygame.image

from code.constants import ENTITY_SPEED, ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.nome = name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.nome]
        self.health = ENTITY_HEALTH[self.nome]

    @abstractmethod
    def move(self):
        pass
