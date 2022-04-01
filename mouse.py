import pygame, sys, random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
#coordenadas del cuadrado
coord_x = 10
coord_y = 10
#velocidad
speed_x = 0
speed_y = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Eventos de teclado
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed_x = -3
        if event.key == pygame.K_RIGHT:
            speed_x = 3
        if event.key == pygame.K_UP:
            speed_y = -3
        if event.key == pygame.K_DOWN:
            speed_y = 3
               
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed_x = 0
        if event.key == pygame.K_RIGHT:
            speed_x = 0
        if event.key == pygame.K_UP:
            speed_y = 0
        if event.key == pygame.K_DOWN:
            speed_y = 0      
            
    screen.fill(WHITE)
    coord_x += speed_x
    coord_y += speed_y
    #mouse events
   # mouse_pos = pygame.mouse.get_pos()
   # x = mouse_pos[0]
   # y = mouse_pos[1]
    #Zona dibjo
    pygame.draw.rect(screen, RED, (coord_x,coord_y,100,100))
    
    
    pygame.display.flip()
    clock.tick(60)