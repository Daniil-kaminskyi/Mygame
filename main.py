import random

import pygame
from window import window
from player import Player
from NPC import NPC
from random import randrange
from background import Star
from menu import Menu

pygame.init()
run = True
font = pygame.font.Font("Graphics/GorgeousPixel.ttf", 30)
text = font.render("score: 0", 0, (255, 255, 255))

npc = NPC(500, 250)
player = Player()
menu = Menu()
time = pygame.time.Clock()
stars = []
for _ in range(20):
    stars.append(Star(randrange(0, 1000), randrange(0, 490)))

x = 500
y = 250
score = 0
while run:
    keys = pygame.key.get_pressed()

    time.tick(60)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if  not menu.is_active:
        if keys[pygame.K_ESCAPE]:
            if menu.is_start:
                menu.is_start = False 

            menu.is_active = True



        for star in stars:
            star.draw()
            star.move()
        npc.draw()
        npc.move()
        window.blit(text, (20, 20))
        player.draw()
        player.move()
        if npc.x < player.x+40<npc.x+80 and npc.y < player.y+40<npc.y+80:
            score += 1
            text = font.render(f"score: {score}", 0, (255, 255, 255))
            npc.x = randrange(0, 900)
            npc.y = randrange(0, 400)
    else:
        menu.draw()

    pygame.display.update()
