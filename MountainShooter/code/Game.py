import pygame

from code.Level import Level
from code.Menu import Menu
from code.constants import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION:
                level = Level(self.window, 'Level1', menu_return)
                level.run()
