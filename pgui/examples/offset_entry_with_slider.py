#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Ciro García <kolterdyx>
# @Date:   15-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 21-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.

####################################################################################
# This example shows how we can use a slider to offset an entry,                   #
# which allows us to read parts of the text that are outside the widget boundaries #
####################################################################################

import pgui
import pygame
import sys

pygame.init()


class Main:
    def __init__(self):
        # Create a screen so we can display our widgets
        self.screen = pygame.display.set_mode((600, 600))

        # Create some widgets
        self.entry = pgui.Entry(self, width=215, func=self.clear)
        self.slider = pgui.Slider(self, length=200, orientation="horizontal")
        self.button = pgui.Button(self, func=sys.exit)

        # Modify some widget values
        self.button.set_label("Exit")
        self.slider.set_label("")
        self.slider.border_width = 1
        self.slider.bg_color = (180, 180, 180)
        self.slider.pointer_color = (100, 100, 100)
        self.slider.pointer_border_width = 1
        self.entry.border_width = 1
        self.button.border_width = 1

        # Move the widgets to the location we want them to be
        self.entry.move(50, 50)
        self.slider.move(50, 80)
        self.button.move(480, 530)

        # This is optional but we can but the widgets inside a list so we can
        # then iterate through it to update the widgets
        self.widgets = [self.entry, self.button, self.slider]

    def clear(self):
        # This will clear the text in the Entry widget
        self.entry.clear()

    def update(self):
        self.screen.fill((200, 200, 200))

        # Update each widget
        for w in self.widgets:
            w.update()

        self.slider.max = self.entry.get_text_pixel_length() - self.entry.width + self.entry.get_font_size()

        if self.entry.get_text_pixel_length() > self.entry.width:
            self.entry.offset = self.slider.mark

        # Update the screen
        pygame.display.flip()

    # We can use a separate method for event handling
    def events(self):
        # The loop does not need to have anything in it but we
        # can use it however we want
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit  # This is just the same as sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit  # This is just the same as sys.exit()


main = Main()
while True:
    main.update()
    main.events()
