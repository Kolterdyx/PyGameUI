# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


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
        # Take the parent's screen to displat the widget
        self.screen = parent.screen
        # Create a rect based on the dimensions given
        self.rect = pg.Rect((x, y), (width, height))
        # Save the values passed
        self.text = text
        self.func = func

        self.font_name = "Arial"
        self.font = pg.font.SysFont("Arial", 20)
        self.font_size = 20
        self.font_color = (0, 0, 0)

        self.border_width = 5
        # Create a slightly bigger rect for the border so it does not cover the widget
        self.border = pg.Rect((self.rect.x - self.border_width + 2, self.rect.y - self.border_width + 2),
                              (self.rect.width + self.border_width, self.rect.height + self.border_width))
        self.border_color = (0, 0, 0)

        # Create an image and fill it with the background color
        self.bgcolor = (255, 255, 255)
        self.image = pg.Surface((self.rect.size)).convert_alpha()
        self.image.fill(self.bgcolor)

        self.valuetopass = valuetopass

        # Create two values to keep track of the user interactions with the button
        self.pressed = False
        self.holding = False

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
        if self.rect.collidepoint(mousepos):
            # If the has just been clicked
            if p1:
                # Set self.pressed to True and make the background colo a little darker to give som visual feedback to the user
                self.pressed = True
                color = (self.bgcolor[0] - 40, self.bgcolor[1] - 40, self.bgcolor[2] - 40)
                self.image.fill(color)
            # If the user is holding the button
            if self.pressed and not self.holding:
                # Set self.holding to True and if there is no function specified, give some feedback to the user via terminal
                # TODO: this can be used to call two different functions. One on press, and one on release
                self.holding = True
                if not self.func:
                    print(self, "has been pressed")

            # If the user releases the button
            if not p1 and self.pressed:
                # Reset the values
                self.pressed = False
                self.holding = False
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
                self.image.fill(self.bgcolor)

        # Render the label with the text, font and color specified
        self.label = self.font.render(self.text, 1, self.font_color)

        # Show everything we need on screen
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.label, (
            self.rect.centerx - self.label.get_rect().width / 2, self.rect.centery - self.label.get_rect().height / 2))
        # Only draw the border if the width is greater than 0
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

        # Try to find a font file using the value as a path
        try:
            self.font = pg.font.Font(font, self.font_size)
            self.font_name = font

        # If it does not find a font file, try finding a font installed in the system
        except FileNotFoundError:
            try:
                self.font_name = font
                self.font = pg.font.SysFont(font, self.font_size)

            # If it also fails, do not change the font and give a warning
            except:
                print("WARNING: Font not found")

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
        # Save border width to variable
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
        # Save the border color to a variable
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
        # Save the text to a variable
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
        # Reposition the widget components
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.border = pg.Rect((self.rect.x - self.border_width + 2, self.rect.y - self.border_width + 2),
                              (self.rect.width + self.border_width, self.rect.height + self.border_width))
