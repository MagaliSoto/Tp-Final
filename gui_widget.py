import pygame
from pygame.locals import *
from constantes import *

class Widget:
    def __init__(self,master_form,x,y,w,h,image_background):
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if image_background != None:
            self.image_background = pygame.image.load(image_background)
            self.image_background = pygame.transform.scale(self.image_background,(w, h))
        else:
            self.image_background = None

    def render(self):
        
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))

    def draw(self):
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)