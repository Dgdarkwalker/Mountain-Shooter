import random

from code.BackGround import BackGround
from code.Enemy import Enemy
from code.Player import Player
from code.constants import LEVEL1_BG_RANGE, WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(LEVEL1_BG_RANGE):
                    lista_bg.append(BackGround(f'Level1Bg{i}', (0, 0)))
                    lista_bg.append(BackGround(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return lista_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 30, WIN_HEIGHT - 30)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 30, WIN_HEIGHT - 30)))
