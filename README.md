# PyGameUI

PyGameUi (or pgui) is a Python library for creating simple GUI's in pygame

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyGameUI.

```bash
pip install pgui
```

You can also install from source this way:
```bash
python3 setup.py install --user
```

## Usage

PyGameUI widgets need a parent class with a screen attribute of type pygame.Surface and an event loop to be used. This is a simple working example:

```python
import pgui
import pygame

pygame.init()


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        entry = pgui.Entry(self)
        button = pgui.Button(self)

        entry.move(50, 50)
        button.move(50, 100)

        self.widgets = [entry, button]

    def update(self):
        self.screen.fill((60, 60, 60))
        for w in self.widgets:
            w.update()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            pass


main = Main()
while True:
    main.update()
    main.events()
```

## Development
This module is still being developed, and it may be unstable or buggy.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
