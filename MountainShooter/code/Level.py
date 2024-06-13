import pygame.display
from pygame import Surface

from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.Menu import Menu


class Level:
    def __init__(self, window, nome: str, menu_option: int):
        self.window: Surface = window
        self.nome = nome
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for event in pygame.event.get():
                Menu.verificar_eventos(event)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
