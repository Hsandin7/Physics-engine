import pygame
import math

class Poligono:     # Poligonoos regulares
    def __init__(self, centro: tuple, radio: int,  n_vertices: int, masa=1, velocidad =(0,0), angulo=0, color=(255,255,255)):
        self.centro = centro
        self.radio = radio
        self.n_vertices = n_vertices
        self.angulo = angulo
        self.masa = masa
        self.velocidad = velocidad
        
        self.color = color
        self.vertices = self.obtener_vertices()
        print(self.vertices)


    def obtener_vertices(self):
        vertices = []
        dif_angulo = 360 / self.n_vertices
        for v in range(0, self.n_vertices):
            x = int(self.centro[0] + math.cos(math.radians(dif_angulo*v + self.angulo)) * self.radio)
            y = int(self.centro[1] + math.sin(math.radians(dif_angulo*v + self.angulo)) * self.radio)
            vertices.append((x,y))
        # print(vertices)
        return vertices
    
    def rotar(self, angulo:int):
        self.angulo += angulo
        self.vertices = self.obtener_vertices()

    def mover(self, x=0, y=0):
        self.centro = (self.centro[0]+x, self.centro[1]+y)
        for n, v in enumerate(self.vertices, 0):
            posx = v[0] + x
            posy = v[1] + y
            self.vertices[n] = (posx, posy)

    def draw(self, screen: pygame.display):
        pygame.draw.polygon(screen, self.color, self.vertices)
    
    def draw_circle(self, screen: pygame.display):
        pygame.draw.circle(screen, (100,100,100), self.centro, self.radio)
    
    def mover_a_raton(self):
        pos_raton = pygame.mouse.get_pos()
        self.centro = pos_raton
        self.vertices = self.obtener_vertices()