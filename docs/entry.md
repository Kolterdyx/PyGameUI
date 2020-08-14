# Entry widget
## class Entry(builtins.object)
Entry widget for recieving user text input.

## Usage:
```python
Entry(parent, *, x=0, y=0, w=100, size=20, font='Arial', border=0, func=None, max_length=0)
```


#### Parameters
`parent: class`  
A python class that has a 'screen' attribute of type 'pygame.Surface'.

`x: int`  
x position in pixels.

`y: int`  
y position in pixels.

`w: int`  
Width of the entry in pixels.

`size: int`  
Font size in pixels.

`font: str`  
Font to be used in the entry.

`border: int`  
Width of the widget's border. Set to 0 to remove the border.

`func: function`  
A function that will be executed when the user presses enter while typing.

`max_length: int`  
Max length in characters. Set to 0 for no limit.

---

## Methods
### `get_text()`
#### Description
Return the text typed in the entry.

#### Parameters
None

#### Returns
`str`

#### Usage
`Entry.get_text()`

---

### `move(x, y)`
#### Description
Change the widget's position

#### Parameters
`x: int`   
Set widget's position along the x axis
`y: int`   
Set widget's position along the y axis

#### Usage:
`Entry.move(200,300)`

---

### `set_bg_color(self, color)`
#### Description
Set the color of the background to 'color'

#### Parameters
`color: tuple`   
A 3-tuple containing an RGB value.

#### Returns
None

#### Usage
`Entry.set_bg_color((43,65,24))`

---

### `set_border_color(self, color)`
#### Description
Set the color of the border around the widget

#### Parameters
`color: tuple`   
A 3-tuple containing an RGB value

#### Returns
None

#### Usage
`Entry.set_border_color((34,45,18))`

---

### `set_border_width(self, width)`
#### Description
Set the width of the border around the entry.
Set to 0 to remove the border entirely.

#### Parameters
`width: int`   
Width in pixels of the border

#### Returns
None

#### Usage
`Entry.set_border_width(5)`

---

### `set_font(self, font)`
#### Description
Change the font of the entry.

#### Parameters
`font: str`   
A font name such as "Arial" or a path to a font file '.ttf' or '.otf'

#### Returns
None

#### Usage
`Entry.set_font("Arial")`

---

### `set_font_color(self, color)`
#### Description
Set the color of the text.

#### Parameters
`color: tuple`   
3-tuple containing an RGB value

#### Returns
None

#### Usage
`Entry.set_font_color((255,30,83))`

---

### `set_font_size(self, size)`
#### Description
Change the font size of the entry.

#### Parameters
`size: int`   
The size in pixels of the font

#### Returns
None

#### Usage
`Entry.set_font_size(12)`

---

### `update(self)`
#### Description
Update and display the widget

#### Parameters
None

#### Returns
None

#### Usage
`Entry.update()`

---
[Go back to index](index.md)
