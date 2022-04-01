import pygame, sys, random
pygame.init()

size = (720,720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

background = pygame.image.load("assets/background.png").convert()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.blit(background, [0,0])
    pygame.display.flip()
    clock.tick(60)
pygame.quit() 