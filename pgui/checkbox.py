# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Last modified by:   kolterdyx
# @Last modified time: 20-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


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
        self.parent = parent
        # Take the parent's screen to display the widget
        self._screen = parent.screen
        self._size = size
        self._x = x
        self._y = y
        self._pos = (self._x, self._y)

        # ------- ATTRIBUTES -------
        # Set the default background color
        self.bg_color = (255, 255, 255)
        # Set the default border width
        self.border_width = 3
        # Set the default border color
        self.border_color = (0, 0, 0)
        # Set the default check mark color
        self.check_color = (0, 200, 0)
        # Set the 'cross' style check mark width
        self.cross_width = 5
        # self.checked will be True only when the box is checked
        self.checked = False
        # Set the default box style and check style
        self.check_style = "fill"
        # Set the default side for the text
        self.label_side = "top"
        # Set the default alignment of the text
        self.label_align = "left"
        self.label_padding = 3
        # --------------------------
        self._sq_border_width = self.border_width

        # Create a surface with the specified size. This will be the background
        self._image = pg.Surface((size, size)).convert_alpha()  # Convert to alpha so it supports transparency

        # Get rect from surface
        self._rect = self._image.get_rect()

        # Create a smaller rect to contain the check mark
        self._check_rect = pg.Rect(x + size / 4, y + size / 4, size - size / 2, size - size / 2) if size % 2 == 0 else pg.Rect(
            x + size / 4 - 1, y + size / 4 - 1, size - size / 2 + 3, size - size / 2 + 3)

        # Move the rect to the proper location
        self._rect.topleft = self._pos

        self._style = "square"

        # self.clicked will be True whenever the primary mouse button is pressed over the widget
        self.clicked = False

        # Set the default text
        self._text = ""
        # Set the default font values
        self._font_size = 20
        self._font_color = (0, 0, 0)
        self._font_name = "Arial"
        self._font = pg.font.SysFont("Arial", self._font_size)

        # Create a label rendering the text with the specified font
        self._label = self._font.render(self._text, 1, self._font_color)

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

        if type(self.check_color) != tuple:
            raise TypeError(".check_color must be a tuple, not", type(self.check_color))
        elif len(self.check_color) != 3:
            raise ValueError("Expected 3 values, got,", len(self.check_color))
        else:
            for i, n in enumerate(self.check_color):
                if type(n) != int:
                    raise ValueError(f"Got type {type(n)} at index {i} instead of int.")

        if type(self.cross_width) != int:
            raise TypeError(".cross_width must be an integer, not", type(self.cross_width))
        elif self.cross_width < 0:
            raise ValueError(".cross_width must be equal or greater than 0.")

        if type(self.checked) != bool:
            raise TypeError(".checked must be a bool, not", type(self.checked))

        if type(self.check_style) != str:
            raise TypeError(".check_style must be a string, not", type(self.check_style))
        elif self.check_style not in ["fill", "cross"]:
            raise ValueError(".check_style must be either \"fill\" or \"cross\"")

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
        """
        #### Description
        Update and draw the widget.

        #### Usage
        `CheckBox.update()`
        """

        self._check_attributes()

        # Detect mouse position and button presses
        # mousepos is a tuple of this format (x, y)
        # p1, p2, p3 are primary click, wheel click and secondary click
        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        # Detect if the widget is being clicked
        if self._rect.collidepoint(mousepos) and p1:
            self.clicked = True

        # Fill the background with the background color
        self._image.fill(self.bg_color)

        # Draw the correct shape corresponding to the style
        if self._style == "square":
            self._screen.blit(self._image, self._rect)
        elif self._style == "circle":
            pg.draw.ellipse(self._screen, self.bg_color, self._rect)
        else:
            raise ValueError("Style must be either \"square\" or \"circle\".")
        # Swap the value of self.checked whenever the box is released from the mouse
        if self.clicked and not p1:
            self.checked = not self.checked
            self.clicked = False

        # Display the check mark if the box is checked depending on the style
        if self.checked:

            # Fill the box if the check style is 'fill'
            if self.check_style == "fill":
                if self._style == "square":
                    pg.draw.rect(self._screen, self.check_color, self._check_rect)
                elif self._style == "circle":
                    pg.draw.ellipse(self._screen, self.check_color, self._check_rect)
            # Draw a cross if the style is 'square' and the check style is 'cross'
            elif self.check_style == "cross":
                if self._style == "square":
                    self._draw_cross()
                elif self._style == "circle":
                    self.check_style = "fill"
            else:
                raise ValueError("Style must be either \"fill\" or \"cross\".")
        # Only show the label if the text string is not empty.
        # Stripping the string will avoid drawing the label if the string contains only invisible characters
        if self._text.strip() != "":
            # Display the label on top of the box
            if self.label_side == "top":
                # Align the label to the left
                if self.label_align == "left":
                    self._screen.blit(self._label, (self._rect.x, self._rect.y - self._font_size - self.label_padding))
                # Align the label to the center
                elif self.label_align == "center":
                    self._screen.blit(self._label, (
                        self._rect.centerx - self._label.get_rect().width / 2, self._rect.y - self._font_size - self.label_padding))
                # Align the label to the right
                elif self.label_align == "right":
                    self._screen.blit(self._label, (
                        self._rect.x + self._rect.width - self._label.get_rect().width, self._rect.y - self._font_size - self.label_padding))

            # Display the label on the bottom of the box
            if self.label_side == "bottom":
                # Align the label to the left
                if self.label_align == "left":
                    self._screen.blit(self._label, (self._rect.x, self._rect.y +
                                                    self._rect.height + self.label_padding))
                # Align the label to the center
                elif self.label_align == "center":
                    self._screen.blit(self._label, (
                        self._rect.centerx - self._label.get_rect().width / 2, self._rect.y + self._rect.height + self.label_padding))
                # Align the label to the right
                elif self.label_align == "right":
                    self._screen.blit(self._label, (
                        self._rect.x + self._rect.width - self._label.get_rect().width, self._rect.y + self._rect.height + self.label_padding))

            # Display the label on the left side of the box
            if self.label_side == "left":
                self._screen.blit(self._label, (self._rect.x - self._label.get_rect().width - self.label_padding,
                                                self._rect.y + self._rect.height - self._label.get_rect().height))
            # Display the label on the right side of the box
            if self.label_side == "right":
                self._screen.blit(self._label, (
                    self._rect.x + self._rect.width + self.label_padding, self._rect.y + self._rect.height - self._label.get_rect().height))

        # Draw a square border if the style is "square" and a round border if the style is "circle"
        if self._style == "square":
            pg.draw.rect(self._screen, self.border_color, self._rect, self.border_width)
        elif self._style == "circle":
            # Modify the dimensions of the check rect to make a good-looking round border
            x = 2 * round((self._x - self.border_width / 2) / 2)
            y = 2 * round((self._y - self.border_width / 2) / 2)
            d = self._rect.width + self.border_width
            d = d + 1 if d % 2 != 0 else d  # Make sure the border' center meets the box center
            pg.draw.ellipse(self._screen, self.border_color, (x, y, d, d), self.border_width)
        else:
            raise ValueError("Style must be either \"square\" or \"circle\".")

    def _draw_cross(self):
        pg.draw.line(self._screen, self.check_color, self._check_rect.topleft,
                     self._check_rect.bottomright, self.cross_width)
        pg.draw.line(self._screen, self.check_color, self._check_rect.bottomleft,
                     self._check_rect.topright, self.cross_width)

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
        if type(x) != int:
            raise TypeError(f"x must be an integer, not {type(x)}")
        if type(y) != int:
            raise TypeError(f"y must be an integer, not {type(y)}")
        # Move the widget
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._rect.topleft = self._pos
        self._check_rect = pg.Rect(x + self._size / 4, y + self._size / 4, self._size - self._size / 2, self._size - self._size / 2) if self._size % 2 == 0 else pg.Rect(
            x + self._size / 4 - 1, y + self._size / 4 - 1, self._size - self._size / 2 + 3, self._size - self._size / 2 + 3)

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

        # Try to use the string as a path to a font.
        # If it does not find a font file, it will raise a FileNotFoundError exception
        if type(font) == str:
            try:
                self._font = pg.font.Font(font, self._font_size)
                # Save the font name or path to a variable
                self._font_name = font

            # We catch the exception and try to find a font installed in the system.
            except FileNotFoundError:
                try:
                    self._font = pg.font.SysFont(font, self._font_size)
                    # Save the font name or path to a variable
                    self._font_name = font

                # If it doesn't find any fonts, we raise a warning saying no font was found
                except:
                    print("WARNING: Font not found")
            self._label = self._font.render(self._text, 1, self._font_color)
        else:
            raise TypeError(f"font must be a string, not {type(font)}")

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

        # If it is not installed, follow a path to the font file
        if type(size) == int:
            try:
                self._font = pg.font.Font(self._font_name, size)

            # If it is installed in the system, use the system one
            except FileNotFoundError:
                self._font = pg.font.SysFont(self._font_name, size)
                # Store the font size in a variable
                self._font_size = size
            self._label = self._font.render(self._text, 1, self._font_color)
        else:
            raise TypeError(f"size must be an integer, not {type(size)}")

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
        `CheckBox.set_font_color((34,13,75))`

        ---

        """
        if type(color) == tuple:
            if len(color) != 3:
                for i, n in enumerate(color):
                    if type(n) == int:
                        continue
                    else:
                        raise TypeError(f"Got type {type(n)} at index {i} instead of int.")
                # Change the font color and re-render the label
                self._font_color = color
                self._label = self._font.render(self._text, 1, color)
            else:
                raise ValueError("Expected 3 values, got", len(color))
        else:
            raise TypeError("color must be a tuple, not", type(color))

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
        if type(size) == int:
            if size > 0:
                # Save the size to a variable and resize and reposition the rects
                self._size = size
                self.check_surface = pg.Surface((self._size - self._size / 10 * 2, self._size -
                                                 self._size / 10 * 2)).convert_alpha()
                self._check_rect = self.check_surface.get_rect()
                self._check_rect.topleft = (self._x + self._size / 10, self._y + self._size / 10)
                self._image = pg.Surface((size, size))
                self._rect = self._image.get_rect()
                self._rect.x = self._x
                self._rect.y = self._y
            else:
                raise ValueError("Size must be greater than 0.")

        else:
            raise TypeError("size must be an integer, not", type(size))

    def set_style(self, style):
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
        # Make sure the style is either "square" or "circle"
        if style not in ["square", "circle"]:
            raise ValueError("style must be either \"square\" or \"circle\".")

        # Change the style of the box
        else:
            self._style = style

            # If the style changes to "circle", change the check style to fill
            # and make the border 1 pixel wider
            if style == "circle":
                self.check_style = "fill"
                self.border_width = self._sq_border_width + 1
                if self._size % 2 != 0:
                    self._check_rect = pg.Rect(self._check_rect.x - 2, self._check_rect.y - 2, self._check_rect.width + 3,
                                               self._check_rect.height + 3)

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
        `CheckBox.set_text("This is a check box")`

        ---

        """
        # Save the text in a variable and re-render the label
        if type(text) == str:
            self._text = text
            self._label = self._font.render(self._text, 1, self._font_color)
        else:
            raise TypeError("text must be a string, not", type(text))
