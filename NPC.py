import random

import pygame
from window import window

pygame.init()


class NPC:
    def __init__(self, x, y):
        self.speed_x = 1
        self.speed_y = 1
        self.time = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("Graphics/sprite4.png")

    def draw(self):
        window.blit(self.sprite, (self.x, self.y))

    def move(self):

        if pygame.time.get_ticks()-self.time > 500:
            if self.x > 900:
                xrange = (-10, 0)
            elif self.x < 100:
                xrange = (1, 10)
            else:
                xrange = (-10, 10)
            if self.y > 400:
                yrange = (-10, 0)
            elif self.y < 100:
                yrange = (1, 10)
            else:
                yrange = (-10, 10)
            self.speed_x = random.randrange(*xrange)
            self.speed_y = random.randrange(*yrange)
            self.time = pygame.time.get_ticks()
        self.y += self.speed_y
        self.x += self.speed_x
