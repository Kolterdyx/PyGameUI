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

## Attributes

| Attribute        | Description                                          | Type                                   | Content example             |
| :--------------- | :--------------------------------------------------- | :------------------------------------- | :--------------             |
|self.bg_color     | RGB color of the background                          |tuple (red: int, green: int, blue: int) |(255,255,255)                |
|self.border_color | RGB color of the border                              |tuple (red: int, green: int, blue: int) |(255,255,255)                |
|self.border_width | Width in pixels of the border                        |int                                     |3                            |
|self.checked			 | If True, the check mark will be displayed            |bool						                         |True   False                 |
|self.check_color	 | RGB color of the check mark                          |tuple (int, int, int)                   |(255, 255, 255)              |
|self.check_style	 | Style of the check mark                              |str                  					         |"fill"   "cross"             |
|self.text_side		 | Side of the widget to display the label              |str		                				         |"top" "left" "right" "bottom"|
|self.text_align	 | Where to align the label                             |str						                         |"left" "center" "right"      |

---

## Methods
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

---
[Go back to index](../index.md)
