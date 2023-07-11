import pygame
from constantes import *
from auxiliar import *
from constantes import *

class Roca:
    def __init__(self, x, y,falling_speed):
        self.toca_suelo = Auxiliar.getSurfaceFromSpriteSheet("images/Objects auxiliares/roca.png", 5, 3, True)
        self.cayendo = Auxiliar.getSurfaceFromSpriteSheet("images/Objects auxiliares/roca cayendo.png", 1, 1, True)

        self.frame = 0
        self.animation = self.cayendo
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.finished = False
        self.falling_speed = falling_speed
        self.collision_threshold = GROUND_LEVEL 

    def do_animation(self, delta_ms, platforms):
        if not self.finished:
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= 100:
                self.tiempo_transcurrido_animation = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0
                    if self.animation == self.toca_suelo:
                        self.finished = True

        if self.animation is self.cayendo:
            self.rect.y += self.falling_speed

            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    if self.rect.bottom - platform.rect.top <= 600:
                        self.rect.y = platform.rect.top - self.rect.height
                        self.animation = self.toca_suelo
                        break
                
    def update(self, delta_ms, platforms):
        if not self.finished:
            self.do_animation(delta_ms, platforms)

    def draw(self, pantalla):
        if not self.finished:
            self.image = self.animation[self.frame]
            pantalla.blit(self.image, self.rect)

class Tumba:
    def __init__(self, x, y,tiempo_ataque,lado):
        self.quieto = Auxiliar.getSurfaceFromSpriteSheet("images/Objects auxiliares/tumba.png",1,1,lado)
        self.ataca = Auxiliar.getSurfaceFromSpriteSheet("images/Objects auxiliares/tumba ataca.png",14,1,lado)

        self.frame = 0
        self.animation = self.quieto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.tiempo_ataque = tiempo_ataque
        self.tiempo_actual = 0
        self.visible = True
        self.ataque = False

    def atacar(self, delta_ms, on_off=True):
        if self.visible:
            self.ataque = on_off
            self.tiempo_actual += delta_ms
            if on_off and self.tiempo_actual >= self.tiempo_ataque:
                self.ataque = True
                self.animation = self.ataca
                self.tiempo_actual = 0
                self.frame = 0
            else:
                self.ataque = False

    def do_animation(self, delta_ms, platforms):
        if self.visible:
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= 100:
                self.tiempo_transcurrido_animation = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0

    def update(self, delta_ms, platforms):
        if self.visible:
            self.do_animation(delta_ms, platforms)
            self.atacar(delta_ms)

    def draw(self, pantalla):
        if self.visible:
            if self.frame < len(self.animation):
                self.image = self.animation[self.frame]
                pantalla.blit(self.image, self.rect)