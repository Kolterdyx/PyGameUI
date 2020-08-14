# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 14-Aug-2020
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
    Entry widget for recieving user text input.
    """

    def __init__(self, parent, *, x=0, y=0, w=100, size=20, font="Arial", border=0, func=None, max_length=0):
        """
        Initialize entry.

        Parameters
        ----------
        parent: class
            A python class that has a 'screen' attribute of type 'pygame.Surface'.
        x: int
            x position in pixels.
        y: int
            y position in pixels.
        w: int
            Width of the entry in pixels.
        size: int
            Font size in pixels.
        font: str
            Font to be used in the entry.
        border: int
            Width of the widget's border. Set to 0 to remove the border.
        func: function
            A function that will be executed when the user presses enter while typing.
        max_length: int
            Max length in characters. Set to 0 for no limit.
        """
        self.parent = parent
        self.rect = pg.Rect((x, y), (w, size + size / 4))
        self.image = pg.Surface(self.rect.size).convert_alpha()
        self.image.fill((255, 255, 255))
        self.bg_color = (255, 255, 255)

        self.width = w

        self.border = pg.Rect((self.rect.x - border + 2, self.rect.y - border + 2),
                              (w + border, self.rect.height + border))
        self.border_width = border
        self.border_color = (0, 0, 0)

        self.cursor = pg.Surface((size / 10, size)).convert_alpha()
        self.cursor.fill((0, 0, 0))
        self.cursor_rect = self.cursor.get_rect()
        self.cursor_rect.x = self.rect.x + 20
        self.cursor_rect.y = self.rect.y + 1

        self.c = 0
        self.cc = 1
        self.type_cooldown = 0
        self.text = ''

        self.size = size
        self.screen = parent.screen
        self.func = func

        self.font = pg.font.SysFont(font, size)
        self.font_color = (0, 0, 0)
        self.font_name = font
        self.font_size = size

        self.label = self.font.render(self.text, 1, self.font_color)
        self.typing = False
        self.keypressed = False
        self.pressing = False

        self.max_length = max_length

    def _add_char(self, char):
        self.keypressed = True
        if self.max_length:
            if len(self.text) < self.max_length:
                self.text += char
                self.label = self.font.render(self.text, 1, self.font_color)
        else:
            self.text += char
            self.label = self.font.render(self.text, 1, self.font_color)

    def _remove_char(self):
        self.keypressed = True
        self.text = self.text[:-1]
        self.label = self.font.render(self.text, 1, self.font_color)

    def update(self):
        """Update and display the widget"""
        if self.c < 100 and self.cc == 1:
            self.c += self.cc
            self.cursor.fill(self.font_color)
        elif self.c > 0 and self.cc == -1:
            self.c += self.cc
            self.cursor.fill((0, 0, 0, 0))
        else:
            self.cc *= -1

        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        keys = pg.key.get_pressed()
        count = 0
        for i in keys:
            count += i
        if count >= 1:
            self.pressing = True
        else:
            self.pressing = False

        if self.typing and not self.keypressed:
            for a in _characters:
                if keys[a]:
                    self._add_char(_characters[a])
            for b in _letters:
                if keys[b] and (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self._add_char(_letters[b][1])
                if keys[b] and not (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self._add_char(_letters[b][0])
            if keys[pg.K_BACKSPACE]:
                self.keypressed = True
                self._remove_char()
            if keys[pg.K_RETURN]:
                self.keypressed = True
                if self.func:
                    self.func()
                else:
                    self.typing = False

        elif self.typing and self.keypressed:
            if self.type_cooldown >= 30 and self.pressing:
                self.keypressed = False
                self.type_cooldown = 0
            else:
                self.type_cooldown += 1
        if self.type_cooldown >= 60 and not self.pressing:
            self.keypressed = False
            self.type_cooldown = 0

        if p1:
            if self.rect.collidepoint(mousepos):
                self.typing = True
            else:
                self.typing = False

        self.label_rect = self.label.get_rect()
        self.label_rect.x = self.rect.height/20 + self.border_width
        self.label_rect.centery = self.rect.height / 2 + self.rect.height/20
        self.cursor_rect.x = self.label_rect.width + self.rect.height/20 + self.border_width
        self.cursor_rect.centery = self.rect.height / 2

        self.image.fill(self.bg_color)
        if self.typing:
            self.image.blit(self.cursor, self.cursor_rect)
        self.image.blit(self.label, self.label_rect)
        self.screen.blit(self.image, self.rect)

        if self.border_width > 0:
            pg.draw.rect(self.screen, self.border_color, self.border, self.border_width)

    def get_text(self):
        """Return the text typed in the entry."""
        return self.text

    def set_font_color(self, color):
        """
        Set the color of the text.

        Parameters
        ----------
        color: tuple
            3-tuple containing an RGB value

        Returns
        -------
        None

        Usage:
        Entry.set_font_color((255,30,83))
        """
        self.font_color = color

    def set_font(self, font):
        """
        Change the font of the entry.

        Parameters
        ----------
        font: str
            A font name such as "Arial" or a path to a font file '.ttf' or '.otf'

        Returns
        -------
        None

        Usage:
        Entry.set_font("Arial")
        """
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

    def set_font_size(self, size):
        """
        Change the font size of the entry.

        Parameters
        ----------
        size: int
            The size in pixels of the font

        Returns
        -------
            None

        Usage:
        Entry.set_font_size(12)
        """
        self.font_size = size
        try:
            self.font = pg.font.SysFont(self.font_name, self.font_size)
        except:
            self.font = pg.font.Font(self.font_name, self.font_size)

        self.rect = pg.Rect(self.pos, (self.width, size + size / 4))
        self.image = pg.Surface(self.rect.size).convert_alpha()

        self.cursor = pg.Surface((size / 10, size)).convert_alpha()
        self.cursor_rect = self.cursor.get_rect()
        self.cursor_rect.x = 20
        self.cursor_rect.y = 1

    def set_bg_color(self, color):
        """
        Set the color of the background to 'color'

        Parameters
        ----------
        color: tuple
            A 3-tuple containing an RGB value.

        Returns
        -------
            None

        Usage:

        """
        self.bg_color = color
        self.image.fill(color)

    def set_border_width(self, width):
        """
        Set the width of the border around the entry.
        Set to 0 to remove the border entirely.

        Parameters
        ----------
        width: int
            Width in pixels of the border

        Returns
        -------
        None

        Usage:
        Entry.set_border_width(5)
        """
        self.border_width = width

    def set_border_color(self, color):
        """
        Set the color of the border around the widget

        Parameters
        ----------
        color: tuple
            A 3-tuple containing an RGB value

        Returns
        -------
        None

        Usage:
        Entry.set_border_color((34,45,18))
        """
        self.border_color = color

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
        Entry.move(200,300)
        """
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.border = pg.Rect((self.rect.x - self.border_width + self.border_width/2, self.rect.y - self.border_width + self.border_width/2),
                              (self.rect.width + self.border_width, self.rect.height + self.border_width))
