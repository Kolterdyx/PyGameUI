# Button Widget
## class Button(builtins.object)
### Description

### Usage
```python
Button(parent, *, x=0, y=0, w=100, h=50, func=None, text='Button', font='Arial', font_size=20, valuetopass=None)
```

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

## Attributes

| Attribute        | Description                                          | Type                                   | Content example |
| :--------------- | :--------------------------------------------------- | :------------------------------------- | :-------------- |
|self.bg_color     | RGB color of the background                          |tuple (red: int, green: int, blue: int) |(255,255,255)    |
|self.border_color | RGB color of the border                              |tuple (red: int, green: int, blue: int) |(255,255,255)    |
|self.border_width | Width in pixels of the border                        |int                                     |3                |
|self.func         | Function to execute when the user presses enter      |function or method                      |builtins.sum     |
|self.valuetopass  | Value to pass to the function self.func              |any                                     |"anythin"        |

---

## Methods
### `move(self, x, y)`
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

### `set_font(self, font)`
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

### `set_font_color(self, color)`
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

### `set_font_size(self, size)`
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


### `set_label(self, text)`
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

### `update(self)`
#### Description
Update and display the widget

#### Usage
`Button.update()`

---
[Go back to index](../index.md)
