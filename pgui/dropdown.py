# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 14-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


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
