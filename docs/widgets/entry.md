# Entry widget
## class Entry(builtins.object)
### Description
Entry widget for recieving user text input.

### Usage:
```python
Entry(parent, *, x=0, y=0, w=100, size=20, border=0, func=None, max_length=0)
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

`border: int`  
Width of the widget's border. Set to 0 to remove the border.

`func: function`  
A function that will be executed when the user presses enter while typing.

`max_length: int`  
Max length in characters. Set to 0 for no limit.

---

## Attributes


| Attribute        | Description                                          | Type                                   | Content example             |
| :--------------- | :--------------------------------------------------- | :------------------------------------- | :-------------------------- |
|self.bg_color     | RGB color of the background                          |tuple (red: int, green: int, blue: int) |(255,255,255)                |
|self.border_color | RGB color of the border                              |tuple (red: int, green: int, blue: int) |(255,255,255)                |
|self.border_width | Width in pixels of the border                        |int                                     |3                            |
|self.func         | Function to execute when the user presses enter      |function or method                      |builtins.sum                 |
|self.label_align	 | Where to align the label                             |str						                         |"left" "center" "right"      |
|self.label_padding| Distance in pixels between the label and the widget  |int                                     | 3                           |
|self.label_side   | Side of the widget to display the label              |str		                				         |"top" "left" "right" "bottom"|
|self.max_length   | Maximum length of the text in characters             |int                                     |100                          |
|self.offset       | Ammount of pixels to the left to move the text label |int                                     |10                           |
|self.text         | The text typed in the entry                          |str                                     |"A string"                   |
|self.typing       | If true, the keys pressed will be typed in the entry |bool                                    |False                        |
|self.width        | Width in pixels of the widget                        |int                                     |200                          |

---

## Methods
### `get_font_size`
#### Description
Return the size in pixels of the font.

#### Parameters
None

#### Returns
`int`

#### Usage
`Entry.get_font_size()`

---

### `move(x, y)`
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
`Entry.move(200,300)`

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
[Go back to index](../index.md)
