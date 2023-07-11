import pygame
from constantes import *
from auxiliar import *
from gui_button import Button
from gui_form import Form
import time

class puntaje:
    def __init__(self,tamaño, x, y, puntaje):
        self.fuente = pygame.font.Font("images/fuente/BacasimeAntique-Regular.ttf", tamaño)
        self.color = (255, 255, 255)
        self.surface = self.fuente.render(puntaje, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.puntaje = puntaje
    
    def update(self, new_puntaje):
        self.puntaje = new_puntaje

    def draw(self,pantalla):
        text = self.fuente.render(str(self.puntaje), True, self.color)
        pantalla.blit(text,self.rect)

class Cronometro:
    def __init__(self,x,y,tamaño):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.fuente = pygame.font.Font("images/fuente/BacasimeAntique-Regular.ttf",tamaño)
        self.tiempo_inicial = time.time()
        self.minutos = 0
        self.pausado = False
        self.tiempo_pausado = 0

    def obtener_tiempo_transcurrido(self):
        if not self.pausado:
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            self.minutos = int(tiempo_transcurrido / 60)
            segundos = int(tiempo_transcurrido % 60)
            tiempo_formateado = f"{self.minutos:02d}:{segundos:02d}"
            return tiempo_formateado
    
    def pausar(self):
        if not self.pausado:
            self.tiempo_pausado += time.time() - self.tiempo_inicial
            self.pausado = True
    
    def reanudar(self):
        if self.pausado:
            self.tiempo_inicial = time.time()
            self.pausado = False

    def draw(self, pantalla):
        tiempo_actual = self.obtener_tiempo_transcurrido()
        texto = self.fuente.render(tiempo_actual, True, self.color)
        pantalla.blit(texto, (self.x, self.y))

