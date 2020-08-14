import pygame as pg

pg.init()


class DropdownList:
    def __init__(self, parent, *, x=0, y=0, values={'Example 1': 0, 'Example 2': 1, 'Example 3': 3}):
        self.parent = parent
        self.screen = parent.screen
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.values = values

    def update(self):
        pass
