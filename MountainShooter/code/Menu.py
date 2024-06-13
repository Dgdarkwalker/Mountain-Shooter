import sys
import pygame.image
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.constants import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:

    def __init__(self, window):

        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBackGround.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                self.verificar_eventos(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and menu_option > 0:
                        menu_option -= 1
                    elif event.key == pygame.K_UP and menu_option == 0:
                        menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_DOWN and menu_option < len(MENU_OPTION) - 1:
                        menu_option += 1
                    elif event.key == pygame.K_DOWN and menu_option == len(MENU_OPTION) - 1:
                        menu_option = 0

                    if event.key == pygame.K_RETURN and menu_option == len(MENU_OPTION) - 1:
                        self.encerrar_programa()
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    @staticmethod
    def encerrar_programa():
        pygame.quit()
        sys.exit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    @staticmethod
    def verificar_eventos(event):
        if event.type == pygame.QUIT:
            Menu.encerrar_programa()
