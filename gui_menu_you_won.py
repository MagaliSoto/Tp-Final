import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background
from gui_menu_nivel1 import FormGameLevel1


class MenuYouWon(Form):
    def __init__(self, name, master_surface, x, y, w, h,ruta, active):
        super().__init__(name, master_surface, x, y, w, h, active)
        self.ruta = ruta
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/gui/fondos/fondo5.png")
    
        self.boton1 = Button(master=self,x=440,y=340,w=218,h=106,image_background="images/gui/botones/botonSi1.png",on_click=self.on_click_boton1,on_click_param=self.ruta)
        self.boton2 = Button(master=self,x=690,y=340,w=218,h=106,image_background="images/gui/botones/botonNo1.png",on_click=self.on_click_boton2,on_click_param="menuPrincipal")
        self.boton3 = Button(master=self,x=550,y=120,w=240,h=105,image_background="images/gui/botones/botonNivel1.png",on_click=self.on_click_boton1,on_click_param="")
                      
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def set_ruta(self,ruta):
        self.ruta = ruta

    def on_click_boton1(self, parametro):
        self.set_active(self.ruta)
    
    def on_click_boton2(self, parametro):
        self.set_active(parametro)
 
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()



