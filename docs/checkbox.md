# CheckBox Widget
## class CheckBox(builtins.object)

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

## Methods

### `get_state(self)`
#### Description
Get the current state of the check box.

#### Parameters
None

#### Returns
`bool`

#### Usage
`CheckBox.get_state()`

---

### `move(self, x, y)`
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

### `set_bg_color(self, color=(255, 255, 255, 255))`
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

### `set_border_color(self, color)`
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

### `set_border_width(self, width)`
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

### `set_check_color(self, color=(0, 200, 0))`
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

### `set_check_style(self, style='fill')`
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

### `set_cross_width(self, width)`
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

### `set_font(self, font)`
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

### `set_font_color(self, color=(0, 0, 0))`
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

### `set_font_size(self, size)`
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

### `set_size(self, size)`
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

### `set_style(self, style='square')`
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

### `set_text(self, text='')`
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

### `update(self)`
#### Description
Update and draw the widget.

#### Usage
`CheckBox.update()`
