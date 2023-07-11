import pygame
from pygame.locals import *

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active

    @staticmethod
    def set_active(name):
        for aux_form in Form.forms_dict.values():
            aux_form.active = False
        Form.forms_dict[name].active = True
    
    @staticmethod
    def get_active():
        for aux_form in Form.forms_dict.values():
            if(aux_form.active):
                return aux_form
        return None

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)
