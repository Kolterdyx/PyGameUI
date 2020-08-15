#!/usr/bin/python3
# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pgui
import pygame
import sys

pygame.init()


class Main:
    def __init__(self):
        # Create a screen so we can display our widgets
        self.screen = pygame.display.set_mode((600, 600))

        # Create some widgets
        self.entry = pgui.Entry(self, func=self.clear)
        self.button = pgui.Button(self, func=sys.exit)
        self.print_button = pgui.Button(self, func=self.print_text, text="Print")

        # Modify some widget values
        self.button.set_label("Exit")

        # Move them to the location we want them to be
        self.entry.move(50, 50)
        self.button.move(50, 100)
        self.print_button.move(200, 50)

        # This is optional but we can but the widgets inside a list so we can
        # then iterate through it to update the widgets
        self.widgets = [self.entry, self.button, self.print_button]

    # Define some functions
    def print_text(self):
        # This will print the text typed in the Entry widget
        print(self.entry.get_text())

    def clear(self):
        # This will clear the text in the Entry widget
        self.entry.clear()

    def update(self):
        self.screen.fill((60, 60, 60))

        # Update each widget
        for w in self.widgets:
            w.update()

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
