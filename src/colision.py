import math
import pygame
from src.poligono import Poligono


def distance_check(p1: Poligono, p2: Poligono):
    v_centros = (p1.centro[0] - p2.centro[0], p1.centro[1] - p2.centro[1])
    l_v_centros = math.sqrt(v_centros[0]**2 + v_centros[1]**2)
    if l_v_centros < p1.radio + p2.radio:
        return True


def collision_check(p1: Poligono, p2: Poligono):
    # Evaluar ejes de ambos polígonos
    for Poligonoo in (p1, p2):
        p0 = Poligonoo.vertices[-1]
        for p1_v in Poligonoo.vertices:
            # Vector del lado y vector normal
            v_lado = (p1_v[0] - p0[0], p1_v[1] - p0[1])
            v_normal = (v_lado[1], -v_lado[0])

            # Normalización (v_unitario)
            l_v_normal = math.sqrt(v_normal[0]**2 + v_normal[1]**2)
            eje = (v_normal[0] / l_v_normal, v_normal[1] / l_v_normal)

            # Visualización del eje normal (Debbuging)
            # p_medio = (int((p0[0] + p1_v[0]) / 2), int((p0[1] + p1_v[1]) / 2))
            # long = 50
            # p_destino_vector = (p_medio[0] + eje[0] * long, p_medio[1] + eje[1] * long)
            # pygame.draw.line(screen, (255, 255, 255), p_medio, p_destino_vector)

            # Comprobar proyección sobre este eje
            solap = solapamiento_eje(p1, p2, eje)
            if solap < 0:
                # Eje separador encontrado -> no colisión
                return False, None
            

    # Si no se encontró ningún eje separador -> colisión
    return True


def solapamiento_eje(Poligono_1: Poligono, Poligono_2: Poligono, eje: tuple):
    # Proyección polígono 1 y 2
    p1min, p1max = proyectar_eje(Poligono_1.vertices, eje)
    p2min, p2max = proyectar_eje(Poligono_2.vertices, eje)

    # Si se solapan hay que determinar el eje con menor solapamiento
    return (min(p1max, p2max) - max(p1min, p2min))

def proyectar_eje(vertices: Poligono, eje: tuple):
    p_min = p_max = dot(eje, vertices[0])
    for pt in vertices:
        res = dot(eje, pt)
        p_min = min(p_min, res)
        p_max = max(p_max, res)
    return p_min, p_max

def actualizar_direccion(p1: Poligono, p2: Poligono):
    v_centros = (p1.centro[0] - p2.centro[0], p1.centro[1] - p2.centro[1])
    l_v_centros = math.sqrt(v_centros[0]**2 + v_centros[1]**2)
    u_centros = (v_centros[0] / l_v_centros, v_centros[1] / l_v_centros)            # n
    
    v_p1 = p1.velocidad[0] - ()









def box_collision(p1: Poligono, p2: Poligono, ancho, alto):
    if p1.centro[0] - p1.radio < 0 or p1.centro[0] + p1.radio > ancho:
        p1.velocidad[0] *= -1

def cambiar_direccion(p1: Poligono, p2: Poligono):
    c1 = p1.centro
    c2 = p2.centro
    m1 = p1.masa
    m2 = p2.masa
    v1 = p1.velocidad
    v2 = p2.velocidad

    # Vector normal del choque
    n = sub(c1,c2)
    long = math.sqrt(n[0]**2 + n[1]**2)
    n = (n[0]/long, n[1]/long)

    # v1 = p1.velocidad - ((2*m2)/(m1+m2)) * 

    v1 = v1 - dot(v1, n)
    v2 = v2 - dot(v2, n)




def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def mul(a, k):
    return (a[0]*k, a[1]*k)