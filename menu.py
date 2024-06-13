import pygame
from window import window

pygame.init()

class Menu:
    def __init__(self):
        self.is_start = True
        self.is_active = True
    def draw(self):
        font = pygame.font.Font("Graphics/GorgeousPixel.ttf", 60)
        title = font.render("Mygame", 0, (255, 255, 255))
        window.blit(title, title.get_rect(center=(500, 100)))
        font2 = pygame.font.Font("Graphics/GorgeousPixel.ttf", 30)
        if self.is_start:
            word = "start"
        else:
            word = "continue"
        title2 = font2.render(f"Press Space to {word} the game", 0, (255, 255, 255))
        window.blit(title2, title2.get_rect(center=(500, 250)))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_active = False

        if self.is_start:
            word = "Menu"
        else:
            word = "Pause"
        title2 = font2.render(f"{word}", 0, (255, 255, 255))
        window.blit(title2, title2.get_rect(center=(500, 150)))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_active = False





