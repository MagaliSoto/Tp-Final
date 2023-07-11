from player import *
from constantes import *
from auxiliar import Auxiliar
from objetos import explosion

class Enemy():
    
    def __init__(self,x,y,ruta_camina,columnas_camina,speed_walk,tiempo_disparo,gravity,frame_rate_ms,move_rate_ms) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(ruta_camina,columnas_camina,1,True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(ruta_camina,columnas_camina,1)
        
        self.contador = 0
        self.frame = 0
        self.lives = 1
        self.move_x = 0
        self.move_y = 0
        self.disparo = tiempo_disparo
        self.speed_walk =  speed_walk
        self.gravity = gravity
        self.animation = self.walk_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.explosion = explosion(x=self.rect.x,y=self.rect.y,width=160,height=160)
        self.is_fall = False
        self.is_shoot = False
        self.visible = True
        self.muerto = False

        self.tiempo_transcurrido_animation = 0
        self.tiempo_diparos = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        self.tiempo_transcurrido = 0
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def receive_shoot(self):
        if self.visible:
            self.lives -= 1
            if self.lives == 0:
                self.muerto = True
                self.visible = False

    def shoot(self, delta_ms, on_off=True):
        if self.visible:
            self.is_shoot = on_off
            self.tiempo_diparos += delta_ms
            if on_off and not self.is_fall and self.tiempo_diparos >= self.disparo:
                self.is_shoot = True
                self.tiempo_diparos = 0
                self.frame = 0
            else:
                self.is_shoot = False
                     

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list) and self.gravity != 0):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                self.explosion.update_position(self.rect.x, self.rect.y)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0

    def update(self,delta_ms,plataform_list):
        if self.visible:
            self.do_movement(delta_ms,plataform_list)
            self.do_animation(delta_ms) 
            self.shoot(delta_ms)
        if self.muerto:
            self.explosion.do_animation(delta_ms)

    def draw(self,screen):
        if self.visible:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
        if self.muerto:
            self.explosion.draw(screen)

    
