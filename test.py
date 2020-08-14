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
