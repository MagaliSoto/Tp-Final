import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background


class MenuNiveles(Form):
    def __init__(self, name, master_surface, x, y, w, h, active):
        super().__init__(name, master_surface, x, y, w, h, active)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/gui/fondos/fondo3.png")

        self.boton1 = Button(master=self,x=50,y=150,w= 360,h=162,image_background="images/gui/botones/boton1.png",on_click=self.on_click_boton1,on_click_param="form_game_L1")
        self.boton2 = Button(master=self,x=250,y=150,w= 360,h=162,image_background="images/gui/botones/boton2.png",on_click=self.on_click_boton1,on_click_param="form_game_L2")
        self.boton3 = Button(master=self,x=450,y=150,w= 360,h=162,image_background="images/gui/botones/boton3.png",on_click=self.on_click_boton1, on_click_param="form_game_L3")
        self.boton4 = Button(master=self,x=570,y=20,w=170,h=71,image_background="images/gui/botones/botonBack.png",on_click=self.on_click_boton1,on_click_param="menuPrincipal")
                                
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)


    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.lista_widget:    
            aux_widget.draw()