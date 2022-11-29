## WARNING
This library is no longer being developed. I made it as a personal project when I was 16 so I could add GUIs to some other projects I had, but I don't recommend using this for anything. I will not accept PRs and I will not read issues. For this reason, I have deleted the project from pypi, so the name `pgui` is available to someone else.

# PyGameUI ![](https://travis-ci.com/Kolterdyx/PyGameUI.svg?branch=master)

PyGameUI (or pgui) is a Python library for creating simple GUIs in pygame

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyGameUI.

```bash
pip install pgui
```

You can also install from source this way:
```bash
python setup.py install
```

## Usage

PyGameUI widgets need a parent class with a screen attribute of type `pygame.Surface` and a pygame event listener to be used. This is a simple working example:

```python
import pgui
import pygame

pygame.init()


class Main:
    def __init__(self):
        # Create a screen attribute
        self.screen = pygame.display.set_mode((600, 600))
        self.entry = pgui.Entry(self)
        self.button = pgui.Button(self, func=self.print_text)

        self.entry.move(50, 50)
        self.button.move(50, 100)

        self.widgets = [self.entry, self.button]

    def print_text(self):
        print(self.entry.text)

    def update(self):
        self.screen.fill((60, 60, 60))
        for w in self.widgets:
            w.update()
        pygame.display.flip()

    def events(self):
        pygame.event.wait()


main = Main()
while True:
    main.update()
    main.events()
```

## Documentation
You can read the documentation [here](https://github.com/Kolterdyx/PyGameUI/wiki)

## Development
Abandoned

## ChangeLog

You can see the change logs [here](https://github.com/Kolterdyx/PyGameUI/blob/master/CHANGELOG.md)

## Contributing
Please do not contribute. The project is abandoned

## License
[MIT](https://choosealicense.com/licenses/mit/)
