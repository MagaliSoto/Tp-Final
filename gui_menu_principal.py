import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background

class MenuPrincipal(Form):
    def __init__(self,name,master_surface, x, y, w, h, active):
        super().__init__(name,master_surface, x, y, w, h, active)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/gui/fondos/fondo1.png")

        self.boton1 = Button(master=self,x=500,y=200,w= 360,h=162,image_background="images/gui/botones/botonJugar.png",on_click=self.on_click_boton1,on_click_param="menuNiveles")
        self.boton2 = Button(master=self,x=500,y=325,w= 360,h=162,image_background="images/gui/botones/botonConfi.png",on_click=self.on_click_boton1,on_click_param="menuConfiguracion")
        self.boton3 = Button(master=self,x=500,y=450,w= 360,h=162,image_background="images/gui/botones/botonSalir.png",on_click=self.on_click_boton2,on_click_param="")
                    
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
 
    def on_click_boton2(self, parametro):
        pygame.quit()
        sys.exit()

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.lista_widget:    
            aux_widget.draw()