# pylint: disable=C0103
# pylint: disable=E1101
import math
import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.display.set_caption('Paint POO')
Icon = pygame.image.load('icono.png')
pygame.display.set_icon(Icon)

class Paint:
    """Define el tamaño de la ventana con los valores de ancho y alto , el color del fondo"""
    def __init__(self, ancho, alto):
        pygame.init()
        self.superficie = pygame.display.set_mode((ancho, alto))
        self.color_fondo = (0, 0, 0)
        self.color = (50, 100, 00)

    def dibujar_linea_horizontal(self, ejex, ejey, longitud):
        """Linea horizontal"""
        for i in range(longitud):
            self.superficie.set_at((ejex + i, ejey), self.color)
        pygame.display.flip()

    def dibujar_linea_vertical(self, ejex, ejey, longitud):
        """Linea vertical"""
        for i in range(longitud):
            self.superficie.set_at((ejex, ejey + i), self.color)
        pygame.display.flip()

    def dibujar_rectangulo(self, ex, ey, ancho, alto):
        
        """Dibuja rectangulo"""
        self.dibujar_linea_horizontal(ex, ey, ancho)
        self.dibujar_linea_vertical(ex, ey, alto)
        self.dibujar_linea_horizontal(ex, ey + alto, ancho)
        self.dibujar_linea_vertical(ex + ancho, ey, alto)
        pygame.display.flip()
    def dibujar_cuadrado(self, x, y, lado):
        
        
        """Dibuja cuadrado"""
        for i in range(lado):
            for j in range(lado):
                self.superficie.set_at((x + i, y + j), self.color)
        pygame.display.flip()

    def dibujar_circulo(self, x_centro, y_centro, radio):
        """Dibuja circulo"""
        for ejex in range(x_centro - radio, x_centro + radio + 1):
            for ejey in range(y_centro - radio, y_centro + radio + 1):
                distancia = math.sqrt((ejex - x_centro) ** 2 + (ejey - y_centro) ** 2)
                if distancia <= radio:
                    self.superficie.set_at((ejex, ejey), self.color)
        pygame.display.flip()

    

    def dibujar_triangulo_escaleno(self, x1, y1, x2, y2, x3, y3):
        """Función para dibujar un triángulo escaleno"""
        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)
        
    def dibujar_triangulo_equilatero(self, x, y, lado):
        """Dibuja triangulo equilatero"""
        altura = lado * math.sqrt(3) / 2
        x1 = int(x)
        y1 = int(y + altura)
        x2 = int(x - lado / 2)
        y2 = int(y)
        x3 = int(x + lado / 2)
        y3 = int(y)

        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)
        
    def dibujar_triangulo_isosceles(self, x, y, base, altura):
        """Dibuja triangulo isoceles"""
        x1 = int(x)
        y1 = int(y)
        x2 = int(x - base / 2)
        y2 = int(y + altura)
        x3 = int(x + base / 2)
        y3 = int(y + altura)

        self.dibujar_linea(x1, y1, x2, y2)
        self.dibujar_linea(x2, y2, x3, y3)
        self.dibujar_linea(x3, y3, x1, y1)

    def dibujar_linea(self, x1, y1, x2, y2):
        """Dibuja linea"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        while x1 != x2 or y1 != y2:
            self.superficie.set_at((int(x1), int(y1)), self.color)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        pygame.display.flip()

    def ejecutar_comandos(self, comandos):
        """Comandos desde archivo de texto , ya que no me agarra desde la consola"""
        with open(comandos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip().split()
                comando = linea[0]

                if comando == "exit":
                    pygame.quit()
                elif comando == "fondo":
                    if len(linea) >= 4:
                        r = int(linea[1])
                        g = int(linea[2])
                        b = int(linea[3])
                        self.color_fondo = (r, g, b)
                        self.superficie.fill(self.color_fondo)
                elif comando == "linea":
                    direccion = linea[1]
                    ejx = int(linea[2])
                    ejy = int(linea[3])
                    longitud = int(linea[4])

                    if direccion == "-h":
                        self.dibujar_linea_horizontal(ejx, ejy, longitud)
                    elif direccion == "-v":
                        self.dibujar_linea_vertical(ejx, ejy, longitud)
                elif comando == "circulo":
                    if len(linea) >= 4:
                        ejex_centro = int(linea[1])
                        ejey_centro = int(linea[2])
                        radio = int(linea[3])
                        self.dibujar_circulo(ejex_centro, ejey_centro, radio)
                elif comando == "triangulo":
                    if len(linea) >= 4:
                        tipo = linea[1]
                        if tipo == "equilatero":
                            ejx = float(linea[2])
                            ejy = float(linea[3])
                            lado = float(linea[4])
                            self.dibujar_triangulo_equilatero(ejx, ejy, lado)
                        elif tipo == "escaleno":
                            ex1 = float(linea[2])
                            ey1 = float(linea[3])
                            ex2 = float(linea[4])
                            ey2 = float(linea[5])
                            ex3 = float(linea[6])
                            ey3 = float(linea[7])
                            self.dibujar_triangulo_escaleno(ex1, ey1, ex2, ey2, ex3, ey3)
                        elif tipo == "isosceles":
                            ejx = float(linea[2])
                            ejy = float(linea[3])
                            base = float(linea[4])
                            altura = float(linea[5])
                            self.dibujar_triangulo_isosceles(ejx, ejy, base, altura)
                elif comando == "cuadrado":
                    if len(linea) >= 4:
                        ejx = int(linea[1])
                        ejy = int(linea[2])
                        lado = int(linea[3])
                        self.dibujar_cuadrado(ejx, ejy, lado)
                elif comando == "rectangulo":
                    if len(linea) >= 5:
                        ejx = int(linea[1])
                        ejy = int(linea[2])
                        ancho = int(linea[3])
                        alto = int(linea[4])
                        self.dibujar_rectangulo(ejx, ejy, ancho, alto)

    def run(self):
        """Verifica que el programa esta corriendo"""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()

def leer_archivo(helpp):
    """Help"""
    with open('ayuda.txt', 'r', encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)

if __name__ == "__main__":
    ancho_pantalla = 800
    alto_pantalla = 600

    programa = Paint(ancho_pantalla, alto_pantalla)
    programa.ejecutar_comandos("comandos.txt")
    leer_archivo("ayuda.txt")
    programa.run()
