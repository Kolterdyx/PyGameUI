# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 16-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pygame as pg


class Slider:
    """
    Slider widget.
    It can be used to select a value from a range from 0 to a maximum value
    """

    def __init__(self, parent, *, x=0, y=0, orientation="horizontal", length=200, max=100):
        """Initialize the Widget"""

        self.parent = parent
        self._screen = parent.screen
        self._orientation = orientation
        self._length = length
        self._size = length + 15
        self._dragging = False
        self._width = 20
        self._x = x
        self._y = y
        self._pos = (x, y)

        # ------- ATTRIBUTES -------
        self.max = max
        self.mark = 0
        self.border_width = 0
        self.border_color = (0, 0, 0)
        self.pointer_color = (128, 128, 128)
        self.pointer_border_color = (0, 0, 0)
        self.pointer_border_width = 0
        self.bg_color = (255, 255, 255)
        # --------------------------

        if self._orientation == "vertical":
            self._rect = pg.Rect(self._pos, (self._width, self._size))
            self._pointer = pg.Surface((self._width, 15)).convert_alpha()
        elif self._orientation == "horizontal":
            self._rect = pg.Rect(self._pos, (self._size, self._width))
            self._pointer = pg.Surface((15, self._width)).convert_alpha()
        else:
            print("Orientation must be either \"vertical\" or \"horizontal\"")
            raise SystemExit

        self._image = pg.Surface(self._rect.size).convert_alpha()
        self._image.fill((255, 255, 255))
        self._pointer.fill((150, 150, 150))
        self._prect = self._pointer.get_rect()
        self._prect.topleft = self._rect.topleft

        self._text = ""
        self._text_side = "top"
        self._text_align = "left"
        self._font_size = 20
        self._font_color = (0, 0, 0)
        self._font = pg.font.SysFont("Arial", self._font_size)
        self._font_name = "Arial"
        self._label = self._font.render(self._text, 1, self._font_color)

    def update(self):
        """Update the widget"""
        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        self._pos = (self._x, self._y)
        self._x, self._y = self._pos

        if self._prect.collidepoint(mousepos) and p1:
            self._dragging = True

        if self._rect.collidepoint(mousepos) and p1:
            if self._orientation == "vertical":
                self._prect.centery = mousepos[1]
            elif self._orientation == "horizontal":
                self._prect.centerx = mousepos[0]

        self._screen.blit(self._image, self._pos)
        if self._orientation == "vertical":
            if self._dragging:
                if self._prect.y >= self._y:
                    if self._prect.y <= self._y + self._size - self._prect.height:
                        self._prect.centery = mousepos[1]
                    else:
                        self._prect.y = self._y + self._size - self._prect.height
                        self._dragging = False
                else:
                    self._prect.y = self._y
                    self._dragging = False

                if not p1:
                    self._dragging = False

        elif self._orientation == "horizontal":

            if self._dragging:
                if self._prect.x >= self._x:
                    if self._prect.x <= self._x + self._size - self._prect.width:
                        self._prect.centerx = mousepos[0]
                    else:
                        self._prect.x = self._x + self._size - self._prect.width
                        self._dragging = False
                else:
                    self._prect.x = self._x
                    self._dragging = False

                if not p1:
                    self._dragging = False
        self._image.fill(self.bg_color)
        pg.draw.rect(self._screen, self.pointer_color, self._prect)

        if self._orientation == "horizontal":
            self.mark = round(((self._prect.x - self._x) / self._length) * self.max)
        elif self._orientation == "vertical":
            self.mark = round(((self._prect.y - self._y) / self._length) * self.max)

        if self.pointer_border_width > 0:
            pg.draw.rect(self._screen, self.pointer_border_color, self._prect, self.pointer_border_width)

        if self.border_width > 0:
            pg.draw.rect(self._screen, self.border_color, self._rect, self.border_width)

        if self._text.strip() != "":
            if self._text_side == "top":
                if self._text_align == "left":
                    self._screen.blit(self._label, (self._rect.x, self._rect.y - self._font_size - 10))
                elif self._text_align == "center":
                    self._screen.blit(self._label, (
                        self._rect.centerx - self._label.get_rect().width / 2, self._rect.y - self._font_size - 10))
                elif self._text_align == "right":
                    self._screen.blit(self._label, (
                        self._rect.x + self._rect.width - self._label.get_rect().width, self._rect.y - self._font_size - 10))
            if self._text_side == "bottom":
                if self._text_align == "left":
                    self._screen.blit(self._label, (self._rect.x, self._rect.y + self._rect.height + 10))
                elif self._text_align == "center":
                    self._screen.blit(self._label, (
                        self._rect.centerx - self._label.get_rect().width / 2, self._rect.y + self._rect.height + 10))
                elif self._text_align == "right":
                    self._screen.blit(self._label, (
                        self._rect.x + self._rect.width - self._label.get_rect().width, self._rect.y + self._rect.height + 10))
            if self._text_side == "left":
                self._screen.blit(self._label, (self._rect.x - self._label.get_rect().width - 10,
                                                self._rect.y + self._rect.height - self._label.get_rect().height))
            if self._text_side == "right":
                self._screen.blit(self._label, (
                    self._rect.x + self._rect.width + 10, self._rect.y + self._rect.height - self._label.get_rect().height))

    def set_label(self, text):
        """
        #### Description
        Set the color of the border around the widget.

        #### Parameters
        `text: str`
        A string for the widget's label.

        #### Returns
        None

        #### Usage
        `Slider.set_label("Some text")`

        ---

        """
        self._text = text
        self._label = self._font.render(text, 1, self._font_color)

    def set_font(self, font):
        """
        #### Description
        Change the font of the widget's label.

        #### Parameters
        `font: str`
        A font name such as "Arial" or a path to a font file '.ttf' or '.otf'.

        #### Returns
        None

        #### Usage
        `Slider.set_font("Arial")`
        """
        self._font_name = font
        try:
            self._font = pg.font.Font(font, self._font_size)
        except:
            self._font = pg.font.SysFont(font, self._font_size)

    def set_font_size(self, size=10):
        """
        #### Description
        Set the size of the widget's label font.

        #### Parameters
        `size: int`
        The label font size in pixels.

        #### Returns
        None

        #### Usage
        `Slider.set_font_size(12)`

        ---

        """
        self._font_size = size
        self._font = pg.font.SysFont(self._font_path, size)

    def set_font_color(self, color=(0, 0, 0)):
        """
        #### Description
        Set the color of the widget's label.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Slider.set_font_color((34,45,18))`

        ---

        """
        self._font_color = color
        self._label = self._font.render(self._text, 1, color)

    def set_width(self, width):
        """
        #### Description
        Set the width of the widget (height if horizontal, width if vertical)

        #### Parameters
        `width: int`
        Width in pixels

        #### Returns
        None

        #### Usage
        `Slider.set_width(20)`

        ---

        """
        self._width = width
        if self._orientation == "vertical":
            self._rect = pg.Rect(self._pos, (self._width, self._size))
            self._pointer = pg.Surface((self._width, 15)).convert_alpha()
        elif self._orientation == "horizontal":
            self._rect = pg.Rect(self._pos, (self._size, self._width))
            self._pointer = pg.Surface((15, self._width)).convert_alpha()
        self._image = pg.Surface(self._rect.size).convert_alpha()
        self._prect = self._pointer.get_rect()
        self._prect.topleft = self._pos

    def set_length(self, length):
        """
        #### Description
        Set the length of the slider (height if vertical, width if horizontal)
        The total length will be 15 pixels greater to include the pointer

        #### Parameters
        `length: int`
        Length in pixels

        #### Returns
        None

        #### Usage
        `Slider.set_length(200)`

        ---

        """

        self._length = length
        self._size = length + 15
        if self._orientation == "vertical":
            self._rect = pg.Rect(self._pos, (self._width, self._size))
            self._pointer = pg.Surface((self._width, 15)).convert_alpha()
        elif self._orientation == "horizontal":
            self._rect = pg.Rect(self._pos, (self._size, self._width))
            self._pointer = pg.Surface((15, self._width)).convert_alpha()
        self._image = pg.Surface(self._rect.size).convert_alpha()

    def move(self, x, y):
        """
        #### Description
        Change the widget's position

        #### Parameters
        `x: int`
        Set widget's position along the x axis
        `y: int`
        Set widget's position along the y axis

        #### Returns
        None

        #### Usage
        `Slider.move(200,300)`
        """
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._rect.topleft = self._pos
        self._prect.topleft = self._pos
