import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background


class MenuGameOver(Form):
    def __init__(self, name, master_surface, x, y, w, h,ruta, active):
        super().__init__(name, master_surface, x, y, w, h, active)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/gui/fondos/fondo4.png")
    
        self.boton1 = Button(master=self,x=400,y=320,w= 300,h=145.8,image_background="images/gui/botones/botonSi.png",on_click=self.on_click_boton1,on_click_param=ruta)
        self.boton2 = Button(master=self,x=650,y=320,w= 300,h=145.8,image_background="images/gui/botones/botonNo.png",on_click=self.on_click_boton2,on_click_param="menuPrincipal")
                                
        self.lista_widget = [self.boton1,self.boton2]

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



