# @Author: kolterdyx
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE.txt', which is part of this source code package.


import pygame as pg

vec = pg.Vector2


class CheckBox:
    """
    ### Description
    A checkable box that can be used to enable or disable functionalities.

    ### Usage
    `CheckBox(parent, *, x=0, y=0, size=20)`

    #### Parameters
    `parent: class`
    A parent class that must have a `screen` attribute of type `pygame.Surface` and an event loop.

    `x: int`
    x position in pixels.

    `y: int`
    y position in pixels.

    `size: int`
    Size (width and height) in pixels.

    ---

    """

    def __init__(self, parent, *, x=0, y=0, size=20):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.parent = parent
        self.screen = parent.screen
        self.size = size
        self.image = pg.Surface((size, size)).convert_alpha()

        self.rect = self.image.get_rect()
        self.check_rect = pg.Rect(x + size / 4, y + size / 4, size - size / 2, size - size / 2) if size % 2 == 0 else pg.Rect(
            x + size / 4 - 1, y + size / 4 - 1, size - size / 2 + 3, size - size / 2 + 3)

        self.rect.topleft = self.pos

        self.bg_color = (255, 255, 255, 255)
        self.border_width = 3
        self.sq_border_width = self.border_width
        self.border_color = (0, 0, 0, 255)

        self.check_color = (0, 200, 0)
        self.cross_width = 5

        self.marked = False
        self.clicked = False

        self.check_style = "fill"
        self.style = "square"

        self.text = ""
        self.text_side = "top"
        self.text_align = "left"
        self.font_size = 20
        self.font_color = (0, 0, 0)
        self.font_name = "Arial"
        self.font = pg.font.SysFont("Arial", self.font_size)
        self.label = self.font.render(self.text, 1, self.font_color)

    def update(self):
        """
        #### Description
        Update and draw the widget.

        #### Usage
        `CheckBox.update()`
        """

        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        if self.rect.collidepoint(mousepos) and p1:
            self.clicked = True
        self.image.fill(self.bg_color)
        if self.style == "square":
            self.screen.blit(self.image, self.rect)
        else:
            pg.draw.ellipse(self.screen, self.bg_color, self.rect)

        if self.clicked and not p1:
            self.marked = not self.marked
            self.clicked = False
        if self.marked:
            if self.check_style == "fill":
                if self.style == "square":
                    pg.draw.rect(self.screen, self.check_color, self.check_rect)
                else:
                    pg.draw.ellipse(self.screen, self.check_color, self.check_rect)
            elif self.check_style == "cross":
                if self.style == "square":
                    self._draw_cross()
                else:
                    self.check_style = "fill"

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

        if self.style == "square":
            pg.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        else:
            x = 2 * round((self.x - self.border_width / 2) / 2)
            y = 2 * round((self.y - self.border_width / 2) / 2)
            d = self.rect.width + self.border_width
            d = d + 1 if d % 2 != 0 else d
            pg.draw.ellipse(self.screen, self.border_color, (x, y, d, d), self.border_width)

    def _draw_cross(self):
        pg.draw.line(self.screen, self.check_color, self.check_rect.topleft,
                     self.check_rect.bottomright, self.cross_width)
        pg.draw.line(self.screen, self.check_color, self.check_rect.bottomleft,
                     self.check_rect.topright, self.cross_width)

    def get_state(self):
        """
        #### Description
        Get the current state of the check box.

        #### Parameters
        None

        #### Returns
        `bool`

        #### Usage
        `CheckBox.get_state()`

        ---

        """
        return self.marked

    def set_text(self, text=""):
        """
        #### Description
        Set the label of the widget.

        #### Parameters
        `text: str`
        A string containing the text to be displayed.

        #### Returns
        None

        #### Usage
        `CheckBox.set_text("This is a check box")`

        ---

        """
        self.text = text
        self.label = self.font.render(self.text, 1, self.font_color)

    def set_font(self, font):
        """
        #### Description
        Set the font for the widget's label.

        #### Parameters
        `font: str`
        A string containing a font name or a path to a font file '.ttf' or '.otf'.

        #### Returns
        None

        #### Usage
        `CheckBox.set_font("Arial")`
        `CheckBox.set_font("path/to/font.ttf")`

        ---

        """
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

    def set_font_size(self, size):
        """
        #### Description
        Set the widget's label font size.

        #### Parameters
        `size: int`
        Font size in pixels.

        #### Returns
        None

        #### Usage
        `CheckBox.set_font_size(12)`

        ---

        """
        self.font = pg.font.SysFont(self.font_path, size)
        self.font_size = size

    def set_font_color(self, color=(0, 0, 0)):
        """
        #### Description
        Set the widget's label font color.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        `CheckBox.set_font_color((34,13,75))`

        ---

        """
        self.font_color = color
        self.label = self.font.render(self.text, 1, color)

    def set_cross_width(self, width):
        """
        #### Description
        Set the cross lines width.
        This will only take effect if the check style is "cross".

        #### Parameters
        `width: int`
        Line width in pixels.

        #### Returns
        None

        #### Usage
        `CheckBox.set_cross_width(4)`

        ---

        """
        self.cross_width = width

    def set_bg_color(self, color=(255, 255, 255, 255)):
        """
        #### Description
        Set the widget's background color.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        `CheckBox.set_bg_color((243,75,43))`

        ---

        """
        self.bg_color = color

    def set_border_color(self, color):
        """
        #### Description
        Set the color of the border around the widget.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        CheckBox.set_border_color((34,45,18))

        ---

        """
        self.border_color = color

    def set_check_style(self, style="fill"):
        """
        #### Description
        Set the style of the check mark.

        #### Parameters
        `style: str`
        A string that must be either `"fill"` or `"cross"`.

        #### Returns
        None

        #### Usage
        `CheckBox.set_check_style("cross")`

        ---

        """
        if style not in ["fill", "cross"]:
            print("Style must be either \"fill\" or \"cross\".")
            raise SystemExit
        else:
            self.check_style = style

    def set_border_width(self, width):
        """
        #### Description
        Set the width of the border around the widget.

        #### Parameters
        `width: int`
        Border width in pixels.
        Set to 0 for no border.

        #### Returns
        None

        #### Usage
        `CheckBox.set_border_width(5)`

        ---

        """
        self.border_width = width
        if self.style == "square":
            self.sq_border_width = width

    def set_border_color(self, color):
        """
        #### Description
        Set the color of the border around the widget.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        `CheckBox.set_border_color((34,45,18))`

        ---

        """
        self.border_color = color

    def set_check_color(self, color=(0, 200, 0)):
        """
        #### Description
        Set the color of the check mark.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        `CheckBox.set_check_color((62,43,187))`

        ---

        """
        self.check_color = color

    def set_size(self, size):
        """
        #### Description
        Set the size of the widget.

        #### Parameters
        `size: int`
        Size (width and height) in pixels.

        #### Returns
        None

        #### Usage
        `CheckBox.set_size(25)`

        ---

        """
        self.size = size
        self.check_surface = pg.Surface((self.size - self.size / 10 * 2, self.size -
                                         self.size / 10 * 2)).convert_alpha()
        self.check_rect = self.check_surface.get_rect()
        self.check_rect.topleft = (self.x + self.size / 10, self.y + self.size / 10)
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_style(self, style="square"):
        """
        #### Description
        Set the check box style.

        #### Parameters
        `style: str`
        A string that must be either "square" or "circle".

        #### Returns
        None

        #### Usage
        `CheckBox.set_style("circle")`

        ---

        """
        if style not in ["square", "circle"]:
            print("Style must be either \"square\" or \"circle\".")
            raise SystemExit
        else:
            self.style = style
            self.check_style = "fill"
            self.border_width = self.sq_border_width + 1
            if self.size % 2 != 0:
                self.check_rect = pg.Rect(self.check_rect.x - 2, self.check_rect.y - 2, self.check_rect.width + 3,
                                          self.check_rect.height + 3)

    def move(self, x, y):
        """
        #### Description
        Change the widget's position.

        #### Parameters
        `x: int`
        Set widget's position along the x axis.
        `y: int`
        Set widget's position along the y axis.

        #### Returns
        None

        #### Usage
        `CheckBox.move(200,300)`

        ---

        """
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.check_rect = pg.Rect(x + self.size / 4, y + self.size / 4, self.size - self.size / 2, self.size - self.size / 2) if self.size % 2 == 0 else pg.Rect(
            x + self.size / 4 - 1, y + self.size / 4 - 1, self.size - self.size / 2 + 3, self.size - self.size / 2 + 3)
