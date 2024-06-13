import pygame
from window import window

pygame.init()


class Player:
    def __init__(self):
        self.speed = 10
        self.x = 500
        self.y = 250
        self.sprite = pygame.image.load("Graphics/sprite3.png")

    def draw(self):
        window.blit(self.sprite, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_d] and self.x < 920:
            self.x += self.speed
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_s] and self.y < 420:
            self.y += self.speed