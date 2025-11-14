import pygame
import sys
from src.poligono import Poligono
from src.colision import *
from src.simulacion import Simulacion2

# Inicializar pygame
pygame.init()

# Configuracion de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naipo")
clock = pygame.time.Clock()


simulacion = Simulacion2(screen)

triangulo = Poligono((screen.get_width()/3,screen.get_height()/2), 100, 3, color=(255,0,0))
cuadrado = Poligono((800,400), 100, 4, color=(0,255,0))

simulacion.objects.append(cuadrado)
simulacion.objects.append(triangulo)


while True:
    eventos = pygame.event.get()
    for event in eventos: 
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))

    cuadrado.draw_circle(screen)
    triangulo.draw_circle(screen)

    simulacion.draw()
    simulacion.update()


    triangulo.mover_a_raton()
    # triangulo.rotar(1)

    pygame.display.flip()
    clock.tick(60)


