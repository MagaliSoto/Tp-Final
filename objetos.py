import pygame
from constantes import *
from auxiliar import *

class Moneda:
    def __init__(self,x, y,width, height) -> None:
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/Objects/moneda/{0}.png",1,9,flip=False,w=width,h=height)
        self.frame = 0
        self.score = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.visible = True

    def obtenida(self,rect_personaje):
        retorno = False

        if(rect_personaje.colliderect(self.rect)and self.visible == True):
            retorno = True
            self.score += 10
            self.visible = False
        return retorno                 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= 100):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self, delta_ms, rect_personaje):
        if self.visible: 
            if not self.obtenida(rect_personaje):
                self.do_animation(delta_ms)

    def draw(self, pantalla):
        if self.visible:
            self.imagen = self.animation[self.frame]
            pantalla.blit(self.imagen, self.rect)

class explosion:
    def __init__(self, x, y,width,height):
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("images/Objects/explosion/{0}.png",1,9,flip=False,w=width,h=height)
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.finished = False  

    def update_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def do_animation(self, delta_ms):
        if not self.finished: 
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= 100:
                self.tiempo_transcurrido_animation = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0
                    self.finished = True 

    def draw(self, pantalla):
        if not self.finished: 
            self.image = self.animation[self.frame]
            pantalla.blit(self.image, self.rect)

class bandera:
    def __init__(self,x,y,width,height) -> None:
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/Objects/bandera/{0}.png",1,2,flip=False,w=width,h=height)
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= 100):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self, delta_ms):
        self.do_animation(delta_ms)

    def draw(self, pantalla):
        self.imagen = self.animation[self.frame]
        pantalla.blit(self.imagen, self.rect) 






