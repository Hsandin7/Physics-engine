import pygame
from src.colision import *

class Simulacion:
    def __init__(self, screen: pygame.display):
        self.objects = []
        self.screen = screen
        
        pygame.font.init()      # Inicializar texto
        self.fuente = pygame.font.SysFont('Arial', 50)


    def update(self):
        obj1 = self.objects[0]
        for num in range(1, len(self.objects)):
            obj2 = self.objects[num]
            if distance_check(obj1, obj2):
                texto = self.fuente.render("Posible colision", True, (255,255,0))
                if collision_check(obj1, obj2):
                    texto = self.fuente.render("Colision", True, (0,255,0))
                    # actualizar_direccion(obj1, obj2)

            else:
                texto = self.fuente.render("No Colision", True, (255,0,0))
            self.screen.blit(texto, (50,50))


    def draw(self):
        for obj in self.objects:
            obj.draw(self.screen)





# class Simulacion2:
#     def __init__(self, screen: pygame.display):
#         self.objects = []
#         self.screen = screen
        
#         pygame.font.init()      # Inicializar texto
#         self.fuente = pygame.font.SysFont('Arial', 50)


#     def update(self):
#         obj1 = self.objects[0]
#         for num in range(1, len(self.objects)):
#             obj2 = self.objects[num]
#             if distance_check(obj1, obj2):
                

#             else:
#                 texto = self.fuente.render("No Colision", True, (255,0,0))
#             self.screen.blit(texto, (50,50))


#     def draw(self):
#         for obj in self.objects:
#             obj.draw(self.screen)