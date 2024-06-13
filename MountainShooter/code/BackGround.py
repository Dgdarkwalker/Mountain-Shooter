from code.Entity import Entity
from code.constants import WIN_WIDTH, ENTITY_SPEED


class BackGround(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
