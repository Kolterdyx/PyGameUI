# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 2-Apr-2021
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pygame as pg
import keyboard


class Entry:
    """
    ### Description
    Entry widget for recieving user text input.

    ### Usage
    `Entry(parent, *, x=0, y=0, width=100, size=20, font='Arial', border=0, func=None, max_length=0)`

    #### Parameters
    `parent: class`
    A python class that has a 'screen' attribute of type 'pygame.Surface'.

    `x: int`
    x position in pixels.

    `y: int`
    y position in pixels.

    `width: int`
    Width of the entry in pixels.

    `size: int`
    Font size in pixels.

    `font: str`
    Font to be used in the entry.

    `border: int`
    Width of the widget's border. Set to 0 to remove the border.

    `func: function`
    A function that will be executed when the user presses enter while typing.

    `max_length: int`
    Max length in characters. Set to 0 for no limit.

    ---

    """

    def __init__(self, parent, *, x=0, y=0, width=100, size=20, border=0, func=None, max_length=0):

        self.parent = parent
        self._rect = pg.Rect((x, y), (width, size + size / 4))
        self._image = pg.Surface(self._rect.size).convert_alpha()
        self._image.fill((255, 255, 255))

        # ------- ATTRIBUTES -------
        self.width = width
        self.border_width = border
        self.border_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.func = func
        self.max_length = max_length
        self.typing = False
        self.offset = 0
        self.text = ''
        self.label_side = "top"
        self.label_align = "left"
        self.label_padding = 3
        self.func = func if func else self.clear
        # --------------------------

        self._x = y
        self._y = y
        self._pos = (x, y)

        self._cursor = pg.Surface((size / 10, size)).convert_alpha()
        self._cursor.fill((0, 0, 0))
        self._cursor_rect = self._cursor.get_rect()

        self._c = 0
        self._cc = 1

        self._font_size = size
        self._screen = parent.screen

        self._font_name = "Arial"
        self._font_color = (0, 0, 0)
        self._font_size = size
        self._font = pg.font.SysFont(self._font_name, self._font_size)

        self._label = self._font.render(self.text, 1, self._font_color)
        self._ltext = ""
        self._tlabel = self._font.render(self._ltext, 1, self._font_color)

        keyboard.on_press(self._add_char)

        self._keywords = {
            "backspace": self._remove_char,
            "esc": self._stop_typing,
            "return": self.func,
            "enter": self.func
        }

        self._letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890º'¡`+´ç,.-;:_¨Ç*^¿?=)(/&%$·\"!ª\\|@#~€¬[]\{\}"

    def _add_char(self, char):
        if self.typing:
            if char.name in self._letters:
                if self.max_length:
                    if len(self.text) < self.max_length:
                        self.text += char.name if char.name != "space" else " "
                else:
                    self.text += char.name if char.name != "space" else " "
            elif char.name in self._keywords:
                self._keywords[char.name]()

    def _stop_typing(self):
        self.typing = False

    def _remove_char(self):
        self.text = self.text[:-1]

    def _check_attributes(self):
        if type(self.bg_color) != tuple:
            raise TypeError(".bg_color must be a tuple, not", type(self.bg_color))
        elif len(self.bg_color) != 3:
            raise ValueError("Expected 3 values, got,", len(self.bg_color))
        else:
            for i, n in enumerate(self.bg_color):
                if type(n) != int:
                    raise ValueError(f"Got type {type(n)} at index {i} instead of int.")

        if type(self.border_width) != int:
            raise TypeError(".border_width must be an integer, not", type(self.border_width))
        elif self.border_width < 0:
            raise ValueError(".border_width must be equal or greater than 0.")

        if type(self.border_color) != tuple:
            raise TypeError(".border_color must be a tuple, not", type(self.border_color))
        elif len(self.border_color) != 3:
            raise ValueError("Expected 3 values, got,", len(self.bg_color))
        else:
            for i, n in enumerate(self.border_color):
                if type(n) != int:
                    raise ValueError(f"Got type {type(n)} at index {i} instead of int.")

        if type(self.label_side) != str:
            raise TypeError(".text_side must be a string, not", type(self.label_side))
        elif self.label_side not in ["top", "left", "right", "bottom"]:
            raise ValueError(".text_side must be in ['top', 'left', 'right', 'bottom']")

        if type(self.label_align) != str:
            raise TypeError(".text_align must be a string, not", type(self.label_align))
        elif self.label_align not in ["left", "center", "right"]:
            raise ValueError(".text_align must be in ['left', 'center', 'right']")

        if type(self.label_padding) != int:
            raise TypeError(".label_padding must be an integer, not", type(self.label_padding))
        elif self.label_padding < 0:
            raise ValueError(".label_padding must be equal or greater than 0.")

    def update(self):
        """Update and display the widget"""

        self._check_attributes()

        self._label = self._font.render(self.text, 1, self._font_color)

        if self._c < 100 and self._cc == 1:
            self._c += self._cc
            self._cursor.fill(self._font_color)
        elif self._c > 0 and self._cc == -1:
            self._c += self._cc
            self._cursor.fill((0, 0, 0, 0))
        else:
            self._cc *= -1

        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        if p1:
            if self._rect.collidepoint(mousepos):
                self.typing = True
            else:
                self.typing = False

        self._label_rect = self._label.get_rect()
        self._label_rect.x = self._rect.height/20 + self.border_width*2 - self.offset
        self._label_rect.centery = self._rect.height / 2 + self._rect.height/20
        self._cursor_rect.x = self._label_rect.width + self._rect.height/20 + self.border_width*2 - self.offset
        self._cursor_rect.centery = self._rect.height / 2

        self._image.fill(self.bg_color)
        if self.typing:
            self._image.blit(self._cursor, self._cursor_rect)
        self._image.blit(self._label, self._label_rect)
        self._screen.blit(self._image, self._rect)

        if self.border_width > 0:
            pg.draw.rect(self._screen, self.border_color, self._rect, self.border_width)

        # change label pos
        if self._ltext.strip() != "":
            if self.label_side == "top":
                if self.label_align == "left":
                    self._screen.blit(self._tlabel, (self._rect.x, self._rect.y - self._font_size - self.label_padding))
                elif self.label_align == "center":
                    self._screen.blit(self._tlabel, (
                        self._rect.centerx - self._label_rect.width / 2, self._rect.y - self._font_size - self.label_padding))
                elif self.label_align == "right":
                    self._screen.blit(self._tlabel, (
                        self._rect.x + self._rect.width - self._label_rect.width, self._rect.y - self._font_size - self.label_padding))
            if self.label_side == "bottom":
                if self.label_align == "left":
                    self._screen.blit(self._tlabel, (self._rect.x, self._rect.y +
                                                     self._rect.height + self.label_padding))
                elif self.label_align == "center":
                    self._screen.blit(self._tlabel, (
                        self._rect.centerx - self._label_rect.width / 2, self._rect.y + self._rect.height + self.label_padding))
                elif self.label_align == "right":
                    self._screen.blit(self._tlabel, (
                        self._rect.x + self._rect.width - self._label_rect.width, self._rect.y + self._rect.height + self.label_padding))
            if self.label_side == "left":
                self._screen.blit(self._tlabel, (self._rect.x - self._label_rect.width - self.label_padding,
                                                 self._rect.y + self._rect.height - self._label_rect.height))
            if self.label_side == "right":
                self._screen.blit(self._tlabel, (self._rect.x + self._rect.width + self.label_padding,
                                                 self._rect.y + self._rect.height - self._label_rect.height))

    def clear(self):
        """
        #### Description
        Clear the text in the entry

        #### Parameters
        None

        #### Returns
        None

        #### Usage
        `Entry.clear()`

        ---

        """
        self.text = ""
        self._label = self._font.render(self.text, 1, self._font_color)

    def get_font_size(self):
        return self._font_size

    def get_text_pixel_length(self):
        """Return the length in pixels of the text"""
        return self._label_rect.width

    def set_label(self, text):
        """
        #### Description
        Set the label of the widget.

        #### Parameters
        `text: str`
        A string containing the text to be displayed.

        #### Returns
        None

        #### Usage
        `Entry.set_label("This is a check box")`

        ---

        """
        if type(text) == str:
            self._ltext = text
            self._tlabel = self._font.render(self._ltext, 1, self._font_color)
        else:
            raise TypeError("text must be a string, not", type(text))

    def set_font(self, font):
        """
        #### Description
        Change the font of the entry.

        #### Parameters
        `font: str`
        A font name such as "Arial" or a path to a font file '.ttf' or '.otf'

        #### Returns
        None

        #### Usage:
        `Entry.set_font("Arial")`

        ---

        """
        try:
            self._font = pg.font.Font(font, self._font_size)
        except:
            self._font = pg.font.SysFont(font, self._font_size)
        self._label = self._font.render(self.text, 1, self._font_color)
        self._tlabel = self._font.render(self._ltext, 1, self._font_color)

    def set_font_color(self, color):
        """
        #### Description
        Set the color of the text.

        #### Parameters
        `color: tuple`
        3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Entry.set_font_color((255,30,83))`

        ---

        """
        if type(color) == tuple:
            if len(color) == 3:
                # Change the font color and re-render the label
                self._font_color = color
                self._label = self._font.render(self.text, 1, color)
                self._tlabel = self._font.render(self._ltext, 1, self._font_color)
            else:
                raise ValueError("Expected 3 values, got", len(color))
        else:
            raise TypeError("color must be a tuple, not", type(color))

    def set_font_size(self, size):
        """
        #### Description
        Change the font size of the entry.

        #### Parameters
        size: int
        The size in pixels of the font

        #### Returns
        None

        #### Usage:
        Entry.set_font_size(12)

        ---

        """
        if type(size) == int:
            try:
                self._font = pg.font.Font(self._font_name, size)

            # If it is installed in the system, use the system one
            except FileNotFoundError:
                self._font = pg.font.SysFont(self._font_name, size)
                # Store the font size in a variable
                self._font_size = size
            self._label = self._font.render(self.text, 1, self._font_color)
            self._tlabel = self._font.render(self._ltext, 1, self._font_color)
        else:
            raise TypeError(f"size must be an integer, not {type(size)}")

        self._rect = pg.Rect(self._pos, (self.width, size + size / 2))
        self._image = pg.Surface(self._rect.size).convert_alpha()

        self._cursor = pg.Surface((size / 10, size)).convert_alpha()
        self._cursor_rect = self._cursor.get_rect()
        self._label = self._font.render(self.text, 1, self._font_color)

    def move(self, x, y):
        """
        #### Description
        Change the widget's position

        #### Parameters
        ----------
        `x: int`
        Set widget's position along the x axis
        `y: int`
        Set widget's position along the y axis

        #### Returns
        -------
        None

        #### Usage:
        `Entry.move(200,300)`

        ---

        """
        if type(x) != int:
            raise TypeError(f"x must be an integer, not {type(x)}")
        if type(y) != int:
            raise TypeError(f"y must be an integer, not {type(y)}")
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._rect.topleft = self._pos
