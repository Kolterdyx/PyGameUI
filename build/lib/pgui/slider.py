# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
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
        self.pborder_color = (0, 0, 0)
        self.pborder_width = 0

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
        """Update the widget"""
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
        if self.pborder_width > 0:
            pg.draw.rect(self.screen, self.pborder_color, self.prect, self.pborder_width)
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
        """
        #### Description
        Return the value marked by the slider

        #### Parameters
        None

        #### Returns
        `int`

        #### Usage
        `Slider.get_mark()`
        """
        if self.orientation == "horizontal":
            mark = ((self.prect.x - self.x) / self.length) * self.max
            return round(mark)
        elif self.orientation == "vertical":
            mark = ((self.prect.y - self.y) / self.length) * self.max
            return round(mark)

    def set_border_width(self, width):
        """
        #### Description
        Set the width of the border around the widget.
        Set to 0 to remove the border entirely.

        #### Parameters
        width: int
        Width in pixels of the border

        #### Returns
        None

        #### Usage
        Slider.set_border_width(5)

        ---

        """
        self.border_width = width

    def set_border_color(self, color):
        """
        #### Description
        Set the color of the border around the widget.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Slider.set_border_color((34,45,18))`

        ---

        """
        self.border_color = color

    def set_pointer_color(self, color):
        """
        #### Description
        Set the color of the selector/pointer.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Slider.set_pointer_color((34,45,18))`

        ---

        """
        self.pointer_color = color

    def set_pointer_border_color(self, color):
        """
        #### Description
        Set the border color of the selector/pointer.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Slider.set_pointer_border_color((34,45,18))`

        ---

        """
        self.pborder_color = color

    def set_pointer_border_width(self, width):
        """
        #### Description
        Set the border width of the selector/pointer.

        #### Parameters
        `width: int`
        The width of the border in pixels

        #### Returns
        None

        #### Usage
        `Slider.set_pointer_border_width(2)`

        ---

        """
        self.pborder_width = width

    def set_bg_color(self, color):
        """
        #### Description
        Set the color of the widget's background.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Slider.set_bg_color((34,45,18))`

        ---

        """
        self.bg_color = color

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
        self.text = text
        self.label = self.font.render(text, 1, self.font_color)

    def set_label_side(self, side):
        """
        #### Description
        Set the relative position of the label to the widget.

        #### Parameters
        `side: str`
        A string from the list ["top", "bottom", "left", "right"]

        #### Returns
        None

        #### Usage
        `Slider.set_label_side("top")`

        ---

        """
        self.text_side = side

    def set_label_alignment(self, alignment):
        """
        #### Description
        Set the alignment of the label when its position is either "top" or "bottom".

        #### Parameters
        `alignment: str`
        A string from the list ["left", "center", "right"]

        #### Returns
        None

        #### Usage
        `Slider.set_label_side("top")`

        ---

        """
        if side in ["left", "center", "right"]:
            self.text_align = alignment
        else:
            raise ValueError("Alignment must be either 'left', 'center' or 'right'")

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
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

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
        self.font_size = size
        self.font = pg.font.SysFont(self.font_path, size)

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
        self.font_color = color
        self.label = self.font.render(self.text, 1, color)

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
        """
        #### Description
        Set maximum value for the selector

        #### Parameters
        `max: int`

        #### Returns
        None

        #### Usage
        `Slider.set_max(50)`

        ---

        """
        self.max = max

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
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.prect.topleft = self.pos
