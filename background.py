import pygame
from window import window

pygame.init()


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("Graphics/star.png")

    def draw(self):
        window.blit(self.sprite, (self.x, self.y))

    def move(self):
        self.y += 10
        if self.y > 510:
            self.y = -20
