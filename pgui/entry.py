# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 16-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pygame as pg

_letters = {
    pg.K_a: ['a', 'A'],
    pg.K_b: ['b', 'B'],
    pg.K_c: ['c', 'C'],
    pg.K_d: ['d', 'D'],
    pg.K_e: ['e', 'E'],
    pg.K_f: ['f', 'F'],
    pg.K_g: ['g', 'G'],
    pg.K_h: ['h', 'H'],
    pg.K_i: ['i', 'I'],
    pg.K_j: ['j', 'J'],
    pg.K_k: ['k', 'K'],
    pg.K_l: ['l', 'L'],
    pg.K_m: ['m', 'M'],
    pg.K_n: ['n', 'N'],
    pg.K_o: ['o', 'O'],
    pg.K_p: ['p', 'P'],
    pg.K_q: ['q', 'Q'],
    pg.K_r: ['r', 'R'],
    pg.K_s: ['s', 'S'],
    pg.K_t: ['t', 'T'],
    pg.K_u: ['u', 'U'],
    pg.K_v: ['v', 'V'],
    pg.K_w: ['w', 'W'],
    pg.K_x: ['x', 'X'],
    pg.K_y: ['y', 'Y'],
    pg.K_z: ['z', 'Z'],
}

_characters = {
    pg.K_SPACE: ' ',
    pg.K_0: '0',
    pg.K_1: '1',
    pg.K_2: '2',
    pg.K_3: '3',
    pg.K_4: '4',
    pg.K_5: '5',
    pg.K_6: '6',
    pg.K_7: '7',
    pg.K_8: '8',
    pg.K_9: '9',
}


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

        # --------------------------

        self._x = y
        self._y = y
        self._pos = (x, y)

        self._cursor = pg.Surface((size / 10, size)).convert_alpha()
        self._cursor.fill((0, 0, 0))
        self._cursor_rect = self._cursor.get_rect()

        self._c = 0
        self._cc = 1
        self._type_cooldown = 0

        self._font_size = size
        self._screen = parent.screen

        self._font_name = "Arial"
        self._font = pg.font.SysFont(font, size)
        self._font_color = (0, 0, 0)
        self._font_size = size

        self._label = self._font.render(self.text, 1, self._font_color)
        self._keypressed = False
        self._pressing = False

    def _add_char(self, char):
        self._keypressed = True
        if self.max_length:
            if len(self.text) < self.max_length:
                self.text += char
        else:
            self.text += char

    def _remove_char(self):
        self._keypressed = True
        self.text = self.text[:-1]

    def update(self):
        """Update and display the widget"""

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

        keys = pg.key.get_pressed()
        count = 0
        for i in keys:
            count += i
        if count >= 1:
            self._pressing = True
        else:
            self._pressing = False

        if self.typing and not self._keypressed:
            for a in _characters:
                if keys[a]:
                    self._add_char(_characters[a])
            for b in _letters:
                if keys[b] and (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self._add_char(_letters[b][1])
                if keys[b] and not (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self._add_char(_letters[b][0])
            if keys[pg.K_BACKSPACE]:
                self._keypressed = True
                self._remove_char()
            if keys[pg.K_RETURN]:
                self._keypressed = True
                if self.func:
                    self.func()
                else:
                    self.typing = False

        elif self.typing and self._keypressed:
            if self._type_cooldown >= 30 and self._pressing:
                self._keypressed = False
                self._type_cooldown = 0
            else:
                self._type_cooldown += 1
        if self._type_cooldown >= 60 and not self._pressing:
            self._keypressed = False
            self._type_cooldown = 0

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

    def get_label_length(self):
        """Return the length in pixels of the label"""
        return self._label_rect.width

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
        self._font_name = font
        try:
            self._font = pg.font.Font(font, self._font_size)
        except:
            self._font = pg.font.SysFont(font, self._font_size)

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
        self._font_color = color

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
        self._font_size = size
        try:
            self._font = pg.font.Font(self._font_name, self._font_size)
        except:
            self._font = pg.font.SysFont(self._font_name, self._font_size)

        self._rect = pg.Rect(self._pos, (self.width, size + size / 4))
        self._image = pg.Surface(self._rect.size).convert_alpha()

        self._cursor = pg.Surface((size / 10, size)).convert_alpha()
        self._cursor_rect = self._cursor.get_rect()

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
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._rect.topleft = self._pos
