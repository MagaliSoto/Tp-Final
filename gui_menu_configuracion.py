import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from constantes import *
from background import Background
from gui_widget import Widget


class MenuConfiguracion(Form):
    def __init__(self,name,master_surface,ruta,x,y,w,h,active):
        super().__init__(name,master_surface,x,y,w,h,active)
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/gui/fondos/fondo2.png")
        self.ruta = ruta
        self.boton1 = Button(master=self,x=450,y=55,w=170,h=71,image_background="images/gui/botones/botonOn.png",on_click=self.on_click_boton1,on_click_param="")
        self.boton2 = Button(master=self,x=450,y=112.5,w=170,h=71,image_background="images/gui/botones/botonOn.png",on_click=self.on_click_boton2,on_click_param="")
        self.boton3 = Button(master=self,x=450,y=170,w=170,h=71,image_background="images/gui/botones/botonBack.png",on_click=self.on_click_boton3,on_click_param=self.ruta)
        
        self.boton1On = True
        self.boton2On = True
        self.lista_widget = [self.boton1,self.boton2,self.boton3]
    
    def set_ruta(self,ruta):
        self.ruta = ruta

    def on_click_boton1(self, parametro):
        if self.boton1On:
            self.boton1 = Button(master=self,x=450,y=55,w=170,h=71,image_background="images/gui/botones/botonOff.png",on_click=self.on_click_boton1,on_click_param="")
            self.boton1On = False
        else:
            self.boton1 = Button(master=self,x=450,y=55,w=170,h=71,image_background="images/gui/botones/botonOn.png",on_click=self.on_click_boton1,on_click_param="")
            self.boton1On = True
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton2(self,parametro):
        if self.boton2On:
            self.boton2 = Button(master=self,x=450,y=112.5,w=170,h=71,image_background="images/gui/botones/botonOff.png",on_click=self.on_click_boton2,on_click_param="")
            self.boton2On = False
        else:
            self.boton2 = Button(master=self,x=450,y=112.5,w=170,h=71,image_background="images/gui/botones/botonOn.png",on_click=self.on_click_boton2,on_click_param="")
            self.boton2On = True

        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton3(self, parametro):
        self.set_active(self.ruta)
        
    def update(self, lista_eventos,keys,delta_ms):
        print(self.ruta)
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()