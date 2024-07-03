from code.BackGround import BackGround
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
                return Player('Player1', (10, WIN_HEIGHT / 2))
