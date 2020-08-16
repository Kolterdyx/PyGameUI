# Widget Documentation

### System Requirements

* Pygame
* Python 3.6 or greater

### Code Requirements

* Pygame imported
* A main class with a `screen` attribute of type `pygame.Surface`
* An update function
* An event loop

#### Minimal code required
```python
import pgui
import pygame

pygame.init()

class Main:
	def __init__(self):
		self.screen = pygame.display.set_mode((600,600))

	def update(self):
		pygame.display.flip()

	def events(self):
		for event in pygame.event.get():
			pass

m = Main()
while True:
	m.update()
	m.events()
```


#### Working example
```python
import pgui
import pygame

pygame.init()


class Main:
	def __init__(self):
		self.screen = pygame.display.set_mode((600, 600))
		entry = pgui.Entry(self)
		button = pgui.Button(self, func=self.print_text)

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
		for event in pygame.event.get():
			pass


main = Main()
while True:
	main.update()
	main.events()
```

---
[Back to README](https://github.com/Kolterdyx/PyGameUI#pygameui)
