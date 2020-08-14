# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 14-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE.txt',\nwhich is part of this source code package.


import pygame as pg
from __init__ import *

pg.init()


class Screen:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.slider = Slider(self)
        self.button = Button(self)
        self.entry = Entry(self, w=300)
        self.checkbox = CheckBox(self)

        self.button.move(20, 20)
        self.slider.move(20, 120)
        self.entry.move(20, 220)
        self.checkbox.move(20, 320)

        self.slider.set_border_width(3)
        self.entry.set_border_width(3)

        self.checkbox.set_check_style("cross")
        self.checkbox.set_check_color((255, 0, 0))

        self.widgets = [self.slider, self.button, self.entry, self.checkbox]

    def run(self):
        self.events()
        self.update()
        self.draw()

    def update(self):
        for w in self.widgets:
            w.update()

        # print(self.slider.get_mark())
        pg.display.flip()

    def draw(self):
        self.screen.fill((100, 100, 50))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    raise SystemExit


s = Screen()
while True:
    s.run()
