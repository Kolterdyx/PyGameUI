# ChangeLog
### 0.0.28
* Added more characters to the Entry and gave it a default function to execute when the return key is pressed.

### 0.0.27
* Fixed a bug in the Slider that moved the pointer back to 0 when the `move()` function was used.

### 0.0.26
* Added functionality to the escape key (deselect the currently selected Entry) and to the return/enter key (execute a function specified with the `self.func` attribue)

### 0.0.25
* Implemented a better solution for adding the characters to the Entry input.

### 0.0.24
* Fixed a bug that registered key strokes even when no Entries were selected.

### 0.0.21
* Added automatic updating to the Entry widget's label.

### 0.0.18
* Fixed a bug in the Entry widget that duplicated the label.

### 0.0.17
* Fixed a fatal error in the `setup.py` file.

### 0.0.14
* Fixed a bug in the `setup.py` file.

### 0.0.10 - 0.0.13
* Added a proper keyboard handler to the Entry widget.
* Fixed a few bugs in all the `set_font_color()` functions involving error handling.

### 0.0.9
* Fixed a bug in the Entry.
* Added tests.

### 0.0.8
* Fixed some bugs in the Slider.
* Added attribute `self.label_padding` to all widgets with an external label.
* Made attribute `self._clicked` "public" (now it is `self.clicked`) for the checkBox.
* Added a label to the Entry.
* Added exceptions.

### 0.0.7.post2
* Another bug.

### 0.0.7.post1
* Sneaky bug I fixed.

### 0.0.7
* Added `set_mark(mark)` method to the slider to handle the change appropiately.

### 0.0.6.post1
* Forgot to update the documentation to the new version

### 0.0.6
* Fixed a new bug in the entry widget.
* Fixed two new bugs in the button widget.
* Added a `get_length()` method to the slider because `_length` shouldn't be directly accessed.
* Added a `get_font_size()` method to the entry widget because `_font_size` shouldn't be directly accessed
* Remodeled the examples

### 0.0.5
* Fixed bugs in the entry widget.
* Removed most of the get/set system because it was stupid (kept some setters to manage some modifications in the correct way).
* Renamed most of the variables to keep track of what is an attribute and what is an implementation.

### 0.0.4
* Fixed another deadly bug in the Button widget
* Added `clear()` method to the Entry widget
* Added `set_offset()` and `get_offset()` methods to the Entry widget
* Added `set_pointer_border_width()` and `set_pointer_border_width` methods to the Slider widget.
* Created two usage examples. (Read more in the [documentation](https://github.com/Kolterdyx/PyGameUI/blob/master/docs/index.md#pygameui-documentation))

### 0.0.3:
* Fixed a deadly bug with the Button widget.
* Added some comments

### 0.0.2
* Added PyDoc

---
[Go back to README.md](README.md)
