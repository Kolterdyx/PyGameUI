# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 15-Aug-2020
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
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.parent = parent
        # Take the parent's screen to display the widget
        self.screen = parent.screen
        self.size = size

        # Create a surface with the specified size. This will be the background
        self.image = pg.Surface((size, size)).convert_alpha()  # Convert to alpha so it supports transparency

        # Get rect from surface
        self.rect = self.image.get_rect()

        # Create a smaller rect to contain the check mark
        self.check_rect = pg.Rect(x + size / 4, y + size / 4, size - size / 2, size - size / 2) if size % 2 == 0 else pg.Rect(
            x + size / 4 - 1, y + size / 4 - 1, size - size / 2 + 3, size - size / 2 + 3)

        # Move the rect to the proper location
        self.rect.topleft = self.pos

        # Set the default background color
        self.bg_color = (255, 255, 255, 255)

        # Set the default border width
        self.border_width = 3

        # Set the 'square' style default border width.
        # This is because when the style is changed to 'circle', the border width is increased by one
        # in order to make it look better, and self.sq_border_width will store the original value
        # in case we change back to 'square'
        self.sq_border_width = self.border_width

        # Set the default border color
        self.border_color = (0, 0, 0)

        # Set the default check mark color
        self.check_color = (0, 200, 0)

        # Set the 'cross' style check mark width
        self.cross_width = 5

        # Create the variables used to manage the interactions.
        # -     self.marked will be True only when the box is checked
        # -     self.clicked will be True whenever the primary mouse button is pressed over the widget
        self.marked = False
        self.clicked = False

        # Set the default box style and check style
        self.check_style = "fill"
        self.style = "square"

        # Set the default text
        self.text = ""
        # Set the default side for the text
        self.text_side = "top"
        # Set the default alignment of the text
        self.text_align = "left"

        # Set the default font values
        self.font_size = 20
        self.font_color = (0, 0, 0)
        self.font_name = "Arial"
        self.font = pg.font.SysFont("Arial", self.font_size)

        # Create some variables to keep some information about the font
        self.font_is_installed = False
        self.font_is_found = False

        # Create a label rendering the text with the specified font
        self.label = self.font.render(self.text, 1, self.font_color)

    def update(self):
        """
        #### Description
        Update and draw the widget.

        #### Usage
        `CheckBox.update()`
        """

        # Detect mouse position and button presses
        # mousepos is a tuple of this format (x, y)
        # p1, p2, p3 are primary click, wheel click and secondary click
        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        # Detect if the widget is being clicked
        if self.rect.collidepoint(mousepos) and p1:
            self.clicked = True

        # Fill the background with the background color
        self.image.fill(self.bg_color)

        # Draw the correct shape corresponding to the style
        if self.style == "square":
            self.screen.blit(self.image, self.rect)
        elif self.style == "circle":
            pg.draw.ellipse(self.screen, self.bg_color, self.rect)

        # Swap the value of self.marked whenever the box is released from the mouse
        if self.clicked and not p1:
            self.marked = not self.marked
            self.clicked = False

        # Display the check mark if the box is checked depending on the style
        if self.marked:

            # Fill the box if the check style is 'fill'
            if self.check_style == "fill":
                if self.style == "square":
                    pg.draw.rect(self.screen, self.check_color, self.check_rect)
                elif self.style == "circle":
                    pg.draw.ellipse(self.screen, self.check_color, self.check_rect)

            # Draw a cross if the style is 'square' and the check style is 'cross'
            elif self.check_style == "cross":
                if self.style == "square":
                    self._draw_cross()
                elif self.style == "circle":
                    self.check_style = "fill"

        # Only show the label if the text string is not empty.
        # Stripping the string will avoid drawing the label if the string contains only invisible characters
        if self.text.strip() != "":
            # Display the label on top of the box
            if self.text_side == "top":
                # Align the label to the left
                if self.text_align == "left":
                    self.screen.blit(self.label, (self.rect.x, self.rect.y - self.font_size - 10))
                # Align the label to the center
                elif self.text_align == "center":
                    self.screen.blit(self.label, (
                        self.rect.centerx - self.label.get_rect().width / 2, self.rect.y - self.font_size - 10))
                # Align the label to the right
                elif self.text_align == "right":
                    self.screen.blit(self.label, (
                        self.rect.x + self.rect.width - self.label.get_rect().width, self.rect.y - self.font_size - 10))

            # Display the label on the bottom of the box
            if self.text_side == "bottom":
                # Align the label to the left
                if self.text_align == "left":
                    self.screen.blit(self.label, (self.rect.x, self.rect.y + self.rect.height + 10))
                # Align the label to the center
                elif self.text_align == "center":
                    self.screen.blit(self.label, (
                        self.rect.centerx - self.label.get_rect().width / 2, self.rect.y + self.rect.height + 10))
                # Align the label to the right
                elif self.text_align == "right":
                    self.screen.blit(self.label, (
                        self.rect.x + self.rect.width - self.label.get_rect().width, self.rect.y + self.rect.height + 10))

            # Display the label on the left side of the box
            if self.text_side == "left":
                self.screen.blit(self.label, (self.rect.x - self.label.get_rect().width - 10,
                                              self.rect.y + self.rect.height - self.label.get_rect().height))
            # Display the label on the right side of the box
            if self.text_side == "right":
                self.screen.blit(self.label, (
                    self.rect.x + self.rect.width + 10, self.rect.y + self.rect.height - self.label.get_rect().height))

        # Draw a square border if the style is "square" and a round border if the style is "circle"
        if self.style == "square":
            pg.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        elif self.style == "circle":
            # Modify the dimensions of the check rect to make a good-looking round border
            x = 2 * round((self.x - self.border_width / 2) / 2)
            y = 2 * round((self.y - self.border_width / 2) / 2)
            d = self.rect.width + self.border_width
            d = d + 1 if d % 2 != 0 else d  # Make sure the border' center meets the box center
            pg.draw.ellipse(self.screen, self.border_color, (x, y, d, d), self.border_width)

    # A simple function to draw a cross
    def _draw_cross(self):
        pg.draw.line(self.screen, self.check_color, self.check_rect.topleft,
                     self.check_rect.bottomright, self.cross_width)
        pg.draw.line(self.screen, self.check_color, self.check_rect.bottomleft,
                     self.check_rect.topright, self.cross_width)

    # Return the self.marked value
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
        # Save the text in a variable and re-render the label
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

        # Try to use the string as a path to a font.
        # If it does not find a font file, it will raise a FileNotFoundError exception
        try:
            self.font = pg.font.Font(font, self.font_size)
            # Save the font name or path to a variable
            self.font_name = font
            self.font_is_installed = False
            self.font_is_found = True

        # We catch the exception and try to find a font installed in the system.
        except FileNotFoundError:
            try:
                self.font = pg.font.SysFont(font, self.font_size)
                # Save the font name or path to a variable
                self.font_name = font

                self.font_is_installed = True
                self.font_is_found = True

            # If it doesn't find any fonts, we raise a warning saying no font was found
            except:
                print("WARNING: Font not found")
                self.font_is_found = False

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

        # Make sure the font is available
        if self.font_is_found:

            # If it is installed in the system, use the system one
            if self.font_is_installed:
                self.font = pg.font.SysFont(self.font_name, size)

            # If it is not installed, follow a path to the font file
            else:
                self.font = pg.font.Font(self.font_name, size)

            # Store the font size in a variable
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

        # Change the font color and re-render the label
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
        # Save the cross width to a variable
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
        # Save the background color to a variable
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
        # Save the border color to a variable
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
        # Make sur the style is either "fill" or "cross"
        if style not in ["fill", "cross"]:
            print("ERROR: Style must be either \"fill\" or \"cross\".")
            raise SystemExit
        else:
            # Save the style to a variable
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
        # Save the border width to a variable
        self.border_width = width
        # If the style is "square", also save it to the square border width
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
        # Save the color to a variable
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
        # Save the check color to a variable
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
        # Save the size to a variable and resize and reposition the rects
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
        # Make sure the style is either "square" or "circle"
        if style not in ["square", "circle"]:
            print("Style must be either \"square\" or \"circle\".")
            raise SystemExit

        # Change the style of the box
        else:
            self.style = style

            # If the style changes to "circle", change the check style to fill
            # and make the border 1 pixel wider
            if style == "circle":
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

        # Move the widget
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.check_rect = pg.Rect(x + self.size / 4, y + self.size / 4, self.size - self.size / 2, self.size - self.size / 2) if self.size % 2 == 0 else pg.Rect(
            x + self.size / 4 - 1, y + self.size / 4 - 1, self.size - self.size / 2 + 3, self.size - self.size / 2 + 3)
