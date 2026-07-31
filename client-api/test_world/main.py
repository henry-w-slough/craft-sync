import pygame
pygame.init()

import random

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256)))

    pygame.display.flip()
    clock.tick(60)
