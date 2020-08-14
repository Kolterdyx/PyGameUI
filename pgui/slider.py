# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 14-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pygame as pg


class Slider:
    def __init__(self, parent, *, x=0, y=0, orientation="horizontal", length=200, max=100):
        self.parent = parent
        self.screen = parent.screen
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.orientation = orientation
        self.length = length
        self.size = length + 15
        self.max = max
        self.dragging = False
        self.width = 20

        if self.orientation == "vertical":
            self.rect = pg.Rect(self.pos, (self.width, self.size))
            self.pointer = pg.Surface((self.width, 15)).convert_alpha()
        elif self.orientation == "horizontal":
            self.rect = pg.Rect(self.pos, (self.size, self.width))
            self.pointer = pg.Surface((15, self.width)).convert_alpha()
        else:
            print("Orientation must be either \"vertical\" or \"horizontal\"")
            raise SystemExit

        self.image = pg.Surface(self.rect.size).convert_alpha()
        self.image.fill((255, 255, 255))
        self.pointer.fill((150, 150, 150))
        self.prect = self.pointer.get_rect()
        self.prect.topleft = self.rect.topleft

        self.border_width = 0
        self.border_color = (0, 0, 0)

        self.pointer_color = (128, 128, 128)

        self.bg_color = (255, 255, 255)

        self.text = "Slider"
        self.text_side = "top"
        self.text_align = "left"
        self.font_size = 20
        self.font_color = (0, 0, 0)
        self.font = pg.font.SysFont("Arial", self.font_size)
        self.font_name = "Arial"
        self.label = self.font.render(self.text, 1, self.font_color)

    def update(self):

        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        if self.prect.collidepoint(mousepos) and p1:
            self.dragging = True

        if self.rect.collidepoint(mousepos) and p1:
            if self.orientation == "vertical":
                self.prect.centery = mousepos[1]
            elif self.orientation == "horizontal":
                self.prect.centerx = mousepos[0]

        self.screen.blit(self.image, self.pos)
        if self.orientation == "vertical":
            if self.dragging:
                if self.prect.y >= self.y:
                    if self.prect.y <= self.y + self.size - self.prect.height:
                        self.prect.centery = mousepos[1]
                    else:
                        self.prect.y = self.y + self.size - self.prect.height
                        self.dragging = False
                else:
                    self.prect.y = self.y
                    self.dragging = False

                if not p1:
                    self.dragging = False

        elif self.orientation == "horizontal":

            if self.dragging:
                if self.prect.x >= self.x:
                    if self.prect.x <= self.x + self.size - self.prect.width:
                        self.prect.centerx = mousepos[0]
                    else:
                        self.prect.x = self.x + self.size - self.prect.width
                        self.dragging = False
                else:
                    self.prect.x = self.x
                    self.dragging = False

                if not p1:
                    self.dragging = False
        self.image.fill(self.bg_color)
        pg.draw.rect(self.screen, self.pointer_color, self.prect)
        if self.border_width > 0:
            pg.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        if self.text.strip() != "":
            if self.text_side == "top":
                if self.text_align == "left":
                    self.screen.blit(self.label, (self.rect.x, self.rect.y - self.font_size - 10))
                elif self.text_align == "center":
                    self.screen.blit(self.label, (
                        self.rect.centerx - self.label.get_rect().width / 2, self.rect.y - self.font_size - 10))
                elif self.text_align == "right":
                    self.screen.blit(self.label, (
                        self.rect.x + self.rect.width - self.label.get_rect().width, self.rect.y - self.font_size - 10))
            if self.text_side == "bottom":
                if self.text_align == "left":
                    self.screen.blit(self.label, (self.rect.x, self.rect.y + self.rect.height + 10))
                elif self.text_align == "center":
                    self.screen.blit(self.label, (
                        self.rect.centerx - self.label.get_rect().width / 2, self.rect.y + self.rect.height + 10))
                elif self.text_align == "right":
                    self.screen.blit(self.label, (
                        self.rect.x + self.rect.width - self.label.get_rect().width, self.rect.y + self.rect.height + 10))
            if self.text_side == "left":
                self.screen.blit(self.label, (self.rect.x - self.label.get_rect().width - 10,
                                              self.rect.y + self.rect.height - self.label.get_rect().height))
            if self.text_side == "right":
                self.screen.blit(self.label, (
                    self.rect.x + self.rect.width + 10, self.rect.y + self.rect.height - self.label.get_rect().height))

    def get_mark(self):
        if self.orientation == "horizontal":
            mark = ((self.prect.x - self.x) / self.length) * self.max
            return round(mark)
        elif self.orientation == "vertical":
            mark = ((self.prect.y - self.y) / self.length) * self.max
            return round(mark)

    def set_border_width(self, width):
        self.border_width = width

    def set_border_color(self, color):
        """
        Set the color of the border around the entry

        Parameters
        ----------
        color: tuple
            A 3-tuple containing an RGB value

        Returns
        -------
        None

        Usage:
        Slider.set_border_color((34,45,18))
        """
        self.border_color = color

    def set_pointer_color(self, color):
        self.pointer_color = color

    def set_bg_color(self, color):
        self.bg_color = color

    def set_text(self, text):
        self.text = text
        self.label = self.font.render(text, 1, self.font_color)

    def set_text_side(self, side):
        self.text_side = side

    def set_text_alignment(self, side):
        self.text_align = side

    def set_font(self, font):
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

    def set_font_size(self, size=10):
        self.font_size = size
        self.font = pg.font.SysFont(self.font_path, size)

    def set_font_color(self, color=(0, 0, 0)):
        self.font_color = color
        self.label = self.font.render(self.text, 1, color)

    def set_width(self, width):
        self.width = width
        if self.orientation == "vertical":
            self.rect = pg.Rect(self.pos, (self.width, self.size))
            self.pointer = pg.Surface((self.width, 15)).convert_alpha()
        elif self.orientation == "horizontal":
            self.rect = pg.Rect(self.pos, (self.size, self.width))
            self.pointer = pg.Surface((15, self.width)).convert_alpha()
        self.image = pg.Surface(self.rect.size).convert_alpha()
        self.prect = self.pointer.get_rect()
        self.prect.topleft = self.pos

    def set_max(self, max):
        self.max = max

    def set_length(self, length):
        self.length = length
        self.size = length + 15
        if self.orientation == "vertical":
            self.rect = pg.Rect(self.pos, (self.width, self.size))
            self.pointer = pg.Surface((self.width, 15)).convert_alpha()
        elif self.orientation == "horizontal":
            self.rect = pg.Rect(self.pos, (self.size, self.width))
            self.pointer = pg.Surface((15, self.width)).convert_alpha()
        self.image = pg.Surface(self.rect.size).convert_alpha()

    def move(self, x, y):
        """
        Change the widget's position

        Parameters
        ----------
        x: int
            Set widget's position along the x axis
        y: int
            Set widget's position along the y axis

        Returns
        -------
        None

        Usage:
        Slider.move(200,300)
        """
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.prect.topleft = self.pos
