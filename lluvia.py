import pygame, sys, random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
size = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        coor_list.append([x,y])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(WHITE)
    for coor in coor_list:
        x = coor[0]
        y = coor[1]
        pygame.draw.circle(screen, RED, (x, y), 2)
        coor[1] +=1
        if coor[1] > 500:
            coor[1] =0
    pygame.display.flip()
    clock.tick(30)