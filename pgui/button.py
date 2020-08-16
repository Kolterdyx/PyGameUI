# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 16-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import pygame as pg

pg.init()


class Button:
    """
    ### Description
    Button widget used to execute functions either on press or on release

    ### Usage
    `Button(parent, *, x=0, y=0, width=100, height=50, _func=None, text="Button", valuetopass=None)`

    #### Parameters
    `x: int`
    x position in pixels.

    `y: int`
    y position in pixels.

    `width: int`
    Width in pixels.

    `height: int`
    Height in pixels.

    `_func: function`
    Function to be called when the button is pressed.

    `text: str`
    Text to display in the button.

    `valuetopass`
    If specified, value to be passed to the function when called.

    ---

    """

    def __init__(self, parent, *, x=0, y=0, width=100, height=50, _func=None, text="Button", valuetopass=None):
        self.parent = parent
        # Take the parent's screen to displat the widget
        self._screen = parent.screen
        # Create a rect based on the dimensions given
        self._rect = pg.Rect((x, y), (width, height))
        # Save the values passed
        self._text = text

        # ------- ATTRIBUTES -------
        self.bg_color = (255, 255, 255)
        self.valuetopass = valuetopass
        self.border_width = 5
        self.border_color = (0, 0, 0)
        self.func = _func
        # --------------------------

        # Create a font
        self._font_name = "Arial"
        self._font_size = 20
        self._font_color = (0, 0, 0)
        self._font = pg.font.SysFont(self._font_name, self._font_size)
        # Create an image and fill it with the background color
        self.image = pg.Surface((self._rect.size)).convert_alpha()
        self.image.fill(self.bg_color)

        # Create two values to keep track of the user interactions with the button
        self._pressed = False
        self._holding = False

    def update(self):
        """
        #### Description
        Update and display the widget

        #### Usage
        `Button.update()`
        """
        # Keep track of the mouse
        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        # If the mouse is over the button
        if self._rect.collidepoint(mousepos):
            # If the has just been clicked
            if p1:
                # Set self._pressed to True and make the background colo a little darker to give som visual feedback to the user
                self._pressed = True
                color = (self.bg_color[0] - 40, self.bg_color[1] - 40, self.bg_color[2] - 40)
                self.image.fill(color)
            # If the user is _holding the button
            if self._pressed and not self._holding:
                # Set self._holding to True and if there is no function specified, give some feedback to the user via terminal
                # TODO: this can be used to call two different functions. One on press, and one on release
                self._holding = True
                if not self.func:
                    print(self, "has been pressed")

            # If the user releases the button
            if not p1 and self._pressed:
                # Reset the values
                self._pressed = False
                self._holding = False
                # If there is not function to call, give some feedback via terminal
                if not self.func:
                    print(self, "has been released")

                # If there is a function
                else:
                    # If we have a value to pass, pass it to the function
                    if self.valuetopass:
                        self.func(self.valuetopass)

                    # Otherwise just call it
                    else:
                        self.func()

                # Set the background color back to the original
                self.image.fill(self.bg_color)

        # Show everything we need on screen
        self._screen.blit(self.image, self._rect)
        self._screen.blit(self._label, (
            self._rect.centerx - self._label.get_rect().width / 2, self._rect.centery - self._label.get_rect().height / 2))
        # Only draw the border if the width is greater than 0
        if self.border_width > 0:
            pg.draw.rect(self._screen, self.border_color, self._rect, self.border_width)

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
        # Reposition the widget components
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._rect.topleft = self._pos

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

        # Try to find a font file using the value as a path
        try:
            self._font = pg.font.Font(font, self._font_size)
            self._font_name = font

        # If it does not find a font file, try finding a font installed in the system
        except FileNotFoundError:
            try:
                self._font_name = font
                self._font = pg.font.SysFont(font, self._font_size)

            # If it also fails, do not change the font and give a warning
            except:
                print("WARNING: Font not found")

        # Render the label with the text, font and color specified
        self._label = self._font.render(self._text, 1, self._font_color)

    def set_font_color(self, color):
        """
        #### Description
        Set the widget's label font color.

        #### Parameters
        `color: tuple`
        A 3-tuple containing an RGB value.

        #### Returns
        None

        #### Usage
        `Button.set_font_color((24,65,247))`

        ---

        """
        self._font_color = color
        self._label = self._font.render(self._text, 1, self._font_color)

    def set_font_size(self, size):
        """
        #### Description
        Set the widget's label font size.

        #### Parameters
        `size: int`
        The size of the font in pixels

        #### Returns
        None

        #### Usage
        `Button.set_font_size(12)`

        ---

        """

        self._font_size = size

        try:
            self._font = pg.font.Font(self._font_name, self._font_size)
        except:
            self._font = pg.font.SysFont(self._font_name, self._font_size)
        # Render the label with the text, font and color specified
        self._label = self._font.render(self._text, 1, self._font_color)

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
        # Save the text to a variable
        self._text = text
        # Render the label with the text, font and color specified
        self._label = self._font.render(self._text, 1, self.font_color)
