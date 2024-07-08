import random
import time

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Menu import Menu
from code.Player import Player
from code.constants import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY


class Level:
    def __init__(self, window, nome: str, menu_option: int):
        self.window: Surface = window
        self.nome = nome
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(f'{self.nome}Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.nome}.mp3')
        pygame.mixer_music.play(-1)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                Menu.verificar_eventos(event)
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            self.level_text(14, f'fps: {clock.get_fps(): .0f}', COLOR_WHITE, (10, 10))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, 25))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
