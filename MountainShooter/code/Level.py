from pygame import Surface


class Level:
    def __init__(self, window, nome: str, option: int):
        self.window: Surface = window
        self.nome = nome
        self.option = option
        self.entity_list = None

    def run(self):
        pass

