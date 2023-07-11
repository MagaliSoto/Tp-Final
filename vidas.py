import pygame
from auxiliar import *
from player import *


class vidas:
    def __init__(self,x, y) -> None:
        self.image_list= Auxiliar.getSurfaceFromSpriteSheet("images/Objects/vidas/fueguito 1.png",12,1,True)
        self.frame = 0
        self.score = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0

    def do_animation(self,delta_ms, personaje):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= 100):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self,delta_ms,personaje):
        self.do_animation(delta_ms,personaje)

    def draw(self, pantalla):
        self.imagen = self.animation[self.frame]
        pantalla.blit(self.imagen, self.rect)

class noVidas:
    def __init__(self,x, y) -> None:
        self.image_list= Auxiliar.getSurfaceFromSpriteSheet("images/Objects/vidas/fueguito 2.png",14,1,True)
        self.frame = 0
        self.score = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.visible = True         

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= 100):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
                self.visible = False
 
    def update(self,delta_ms):
        if self.visible == True:
            self.do_animation(delta_ms)

    def draw(self, pantalla):
        if self.visible == True:
            self.imagen = self.animation[self.frame]
            pantalla.blit(self.imagen, self.rect)





