# @Author: kolterdyx
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE.txt', which is part of this source code package.


import pygame as pg

pg.init()


class Button:
    """
    ### Description
    Button widget used to execute functions either on press or on release

    ### Usage
    `Button(parent, *, x=0, y=0, width=100, height=50, func=None, text="Button", valuetopass=None)`

    #### Parameters
    `x: int`
    x position in pixels.

    `y: int`
    y position in pixels.

    `width: int`
    Width in pixels.

    `height: int`
    Height in pixels.

    `func: function`
    Function to be called when the button is pressed.

    `text: str`
    Text to display in the button.

    `valuetopass`
    If specified, value to be passed to the function when called.

    ---

    """

    def __init__(self, parent, *, x=0, y=0, width=100, height=50, func=None, text="Button", valuetopass=None):
        self.parent = parent
        self.rect = pg.Rect((x, y), (w, h))
        self.text = text
        self.func = func
        self.font = pg.font.SysFont(font, font_size)

        self.font_size = font_size
        self.font_color = (0, 0, 0)

        self.bgcolor = (255, 255, 255)
        self.border_width = 5
        self.border = pg.Rect((self.rect.x - self.border_width + 2, self.rect.y - self.border_width + 2),
                              (w + self.border_width, self.rect.height + self.border_width))
        self.border_color = (0, 0, 0)

        self.image = pg.Surface((self.rect.size)).convert_alpha()
        self.image.fill(self.bgcolor)

        self.pressed = False

        self.screen = parent.screen
        self.already_pressed = False

    def update(self):
        """
        #### Description
        Update and display the widget

        #### Usage
        `Button.update()`
        """
        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        if self.rect.collidepoint(mousepos):
            if p1:
                self.pressed = True
                color = (self.bgcolor[0] - 40, self.bgcolor[1] - 40, self.bgcolor[2] - 40)
                self.image.fill(color)
            if self.pressed and not self.already_pressed:
                self.already_pressed = True
                if not self.func:
                    print(self, "has been pressed")
            if not p1 and self.pressed:
                self.pressed = False
                self.already_pressed = False
                if not self.func:
                    print(self, "has been released")
                else:
                    if self.valuetopass:
                        self.func(self.valuetopass)
                    else:
                        self.func()
                self.image.fill(self.bgcolor)

        self.label = self.font.render(self.text, 1, self.font_color)

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.label, (
            self.rect.centerx - self.label.get_rect().width / 2, self.rect.centery - self.label.get_rect().height / 2))
        if self.border_width > 0:
            pg.draw.rect(self.screen, self.border_color, self.border, self.border_width)

    def set_font_color(self, color):
        """
        #### Description
        Set color of the widget's label font

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Button.set_font_color`

        ---

        """
        self.font_color = color

    def set_font(self, font):
        """
        #### Description
        Set the widget's label font.

        #### Parameters
        `font: str`
        A string containing either a font name or a path to a font file '.ttf' or '.otf'

        #### Returns
        None

        #### Usage
        `Button.set_font("Arial")`
        `Button.set_font("path/to/font.ttf")`

        ---

        """
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

    def set_bg_color(self, color):
        """
        #### Description
        Set the background color of the widget

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Button.set_bg_color((43,63,255))`

        ---

        """
        self.bgcolor = color
        self.image.fill(color)

    def set_border_width(self, width):
        """
        #### Description
        Set the width of the border around the widget

        #### Parameters
        `width: int`
        Border width in pixels.
        Set to 0 for no border

        #### Returns
        None

        #### Usage
        `Button.set_border_width(5)`

        ---

        """
        self.border_width = width

    def set_border_color(self, color):
        """
        #### Description
        Set the color of the border around the widget

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value

        #### Returns
        None

        #### Usage
        `Button.set_border_color((34,45,18))`

        ---

        """
        self.border_color = color

    def set_label(self, text):
        """
        #### Description
        Set the widget's label

        #### Parameters
        `text: str`
        A string with the text to be displayed

        #### Returns
        None

        #### Usage
        Button.set_label("This is a button")

        ---

        """
        self.text = text

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
        `Button.move(200,300)`

        ---

        """
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.border = pg.Rect((self.rect.x - self.border_width + 2, self.rect.y - self.border_width + 2),
                              (self.rect.width + self.border_width, self.rect.height + self.border_width))
