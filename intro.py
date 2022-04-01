import pygame, sys

#Definir Colores

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
#Crea el tamaño en una tupla
size = (800, 500)
#Crea ventana
screen = pygame.display.set_mode(size)
#Permite controlar los fps
clock = pygame.time.Clock()
#Un juego es un bucle infinito

#Coordenadas
cord_x = 400
cord_y = 200

speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()
            
    #------ Logica de juego
    
    #------ Logica del juego
    #Color de fondo
    screen.fill(WHITE)
    ### ------- Zona de dibujo -----------
    """pygame.draw.line(screen, GREEN, [0,100], [200,300],5 )
    #los dos primeros van a ser la poscion y los otros dos la posicion
    pygame.draw.rect(screen, BLACK, (100,100,80,80))
    pygame.draw.circle(screen, RED, (100,200), 30)
    
    for x in range(100,700,100):
        pygame.draw.rect(screen, BLACK, (x,230,50,50))
    """
    """Animaciones"""
    if(cord_x > 720 or cord_x <0):
        speed_x *=-1
    cord_x += speed_x
    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
    
    
    
    ### ------- Zona de dibujo -----------
    #Actualiza la pantalla
    pygame.display.flip()
    clock.tick(60)