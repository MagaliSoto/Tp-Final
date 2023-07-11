import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from objetos import *
from objetos_auxiliares import *
from background import Background
from bullet import Bullet
from vidas import * 
from puntajeYcronometro import *
from generadores_objetos import *


class FormGameLevel2(Form):
    def __init__(self,name,master_surface,x,y,w,h,active):
        super().__init__(name,master_surface,x,y,w,h,active)
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/nivel2.png")
        self.inicio_pantalla = True
        self.flag = False
    def reset(self):
        
        self.flag = True
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=200,y=550,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=250,y=550,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=300,y=550,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=350,y=550,width=50,height=50,type=2))  

        self.plataform_list.append(Plataform(x=350,y=450,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=400,y=450,width=50,height=50,type=13))    
        self.plataform_list.append(Plataform(x=450,y=450,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=500,y=450,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=600,y=400,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=650,y=400,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=750,y=400,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=400,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=900,y=350,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=950,y=350,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=1050,y=300,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=1100,y=300,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=1150,y=300,width=50,height=50,type=2)) 

        self.plataform_list.append(Plataform(x=1220,y=200,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=1270,y=200,width=50,height=50,type=14)) 
        
        self.monedas_lista = []
        self.monedas_lista.append(Moneda(x=200,y=500,width=30,height=30))
        self.monedas_lista.append(Moneda(x=275,y=500,width=30,height=30))
        self.monedas_lista.append(Moneda(x=350,y=500,width=30,height=30))
        
        self.monedas_lista.append(Moneda(x=450,y=400,width=30,height=30))
        self.monedas_lista.append(Moneda(x=500,y=400,width=30,height=30))

        self.monedas_lista.append(Moneda(x=765,y=350,width=30,height=30))
        self.monedas_lista.append(Moneda(x=815,y=350,width=30,height=30))

        self.monedas_lista.append(Moneda(x=930,y=300,width=30,height=30))

        self.monedas_lista.append(Moneda(x=1050,y=250,width=30,height=30))
        self.monedas_lista.append(Moneda(x=1100,y=250,width=30,height=30))
        self.monedas_lista.append(Moneda(x=1150,y=250,width=30,height=30))

        self.bullet_list = []
        self.player_1 = Player(x=5,y=400,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
        
        self.enemy_list = []
        self.rocas_list = [] 

        self.generator = EnemyGenerator(x_range=(50,1250),y_range=(50, 500),cantidad_enemigos=2,speed_range=(1.0, 2.0),shoot_interval_range=(5000,10000),ruta_camina="images/caracters/enemies/enemigo pez.png",columnas_camina=6,gravity=14,puntaje=25)
        self.generatorRoca = RocaGenerator(x_range=(20,1200),gravity_range=[4,8],cantidad_rocas=3)

        for _ in range(2):
            enemy = self.generator.generate_enemy()
            self.enemy_list.append(enemy)
            
        for _ in range(3):
            roca = self.generatorRoca.generate_roca()
            self.rocas_list.append(roca)

        self.player_list = []
        self.player_list.append(self.player_1)

        self.vidas_list = []
        self.vidas_list.append(vidas(x=0,y=3))
        self.vidas_list.append(vidas(x=70,y=3))
        self.vidas_list.append(vidas(x=140,y=3))

        self.no_vidas_list = []
        self.no_vidas_list.append(noVidas(x=0,y=3))
        self.no_vidas_list.append(noVidas(x=70,y=3))
        self.no_vidas_list.append(noVidas(x=140,y=3))

        self.bandera = bandera(1265,150,50,50)

        self.puntos = 0

        self.puntaje = puntaje(tamaño=80,x=1200,y=3,puntaje=str(self.puntos))
        self.cronometro = Cronometro(x=600,y=3,tamaño=80)

        self.boton1 = Button(master=self,x=570,y=-2,w=240,h=105,image_background="images/gui/botones/botonNivel2.png",on_click=self.on_click_boton1,on_click_param="menuPausa")
       

    def disparo_enemigo(self,indice):
        self.bullet_list.append(Bullet("ENEMIGO",self.enemy_list[indice].rect.centerx,self.enemy_list[indice].rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,"images/Objects/fireball.gif",frame_rate_ms=100,move_rate_ms=20,width=15,height=15))

    def disparo_jugador(self):
        for player_element in self.player_list:
            if player_element.direction == DIRECTION_R:
                x_end = player_element.rect.right
                y_end = player_element.rect.centery
            else:
                x_end = player_element.rect.left
                y_end = player_element.rect.centery
            self.bullet_list.append(Bullet("JUGADOR", player_element.rect.centerx, player_element.rect.centery, x_end, y_end, 20, "images/Objects/fireball.gif", frame_rate_ms=100, move_rate_ms=20, width=15, height=15))

    def on_click_boton1(self, parametro):
        self.cronometro.pausar()
        self.set_active(parametro)
        self.cronometro.reanudar()

    def update(self,lista_eventos,keys,delta_ms):
        if self.inicio_pantalla == True:
            self.reset()
            self.inicio_pantalla = False

        if self.player_1.muerto == True or self.cronometro.minutos == 1:
            self.set_active("menuGameOver")
            self.reset()

        if(self.player_1.rect.colliderect(self.bandera.rect)):
            self.set_active("menuYouWon")
            self.reset()
            self.flag = False

        for roca in self.rocas_list:
            if(self.player_1.rect.colliderect(roca.rect)):
                roca.animation = roca.toca_suelo
                self.player_1.lives -=1
        print(self.player_1.lives)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)
        
        for moneda in self.monedas_lista:
            moneda.update(delta_ms,self.player_1.rect)

        match self.player_1.lives:
            case 3:
                for vida in self.vidas_list:
                    vida.update(delta_ms,self.player_1)
            case 2:
                for i in range(len(self.vidas_list)-1):
                    self.vidas_list[i].update(delta_ms,self.player_1)
                self.no_vidas_list[2].update(delta_ms)
            case 1:
                self.vidas_list[0].update(delta_ms,self.player_1)
                self.no_vidas_list[1].update(delta_ms)
            case 0:
                self.no_vidas_list[0].update(delta_ms)

        for indice in range(len(self.enemy_list)):
            if self.enemy_list[indice].is_shoot:
                self.disparo_enemigo(indice)
        
        if self.player_1.is_shoot == True:
            self.disparo_jugador()
        
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        for roca in self.rocas_list:
            roca.update(delta_ms,self.plataform_list)


        self.puntos = sum(moneda.score for moneda in self.monedas_lista)
        self.puntos += self.generator.score
        self.puntaje.update(str(self.puntos))
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)
        self.generator.update(delta_ms,self.enemy_list)
        self.generatorRoca.update(delta_ms,self.rocas_list)
        self.bandera.update(delta_ms)
        self.boton1.update(lista_eventos)


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        match self.player_1.lives:
            case 3:
                for vida in self.vidas_list:
                    vida.draw(self.surface)
            case 2:
                for i in range(len(self.vidas_list)-1):
                    self.vidas_list[i].draw(self.surface)
                self.no_vidas_list[2].draw(self.surface)
            case 1:
                self.vidas_list[0].draw(self.surface)
                self.no_vidas_list[1].draw(self.surface)
            case 0:
                self.no_vidas_list[0].draw(self.surface)

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)
        
        for moneda in self.monedas_lista:
            moneda.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
        
        for roca in self.rocas_list:
            roca.draw(self.surface)
            
        self.player_1.draw(self.surface)
        self.puntaje.draw(self.surface)
        self.boton1.draw()
        self.cronometro.draw(self.surface)
        self.bandera.draw(self.surface)






