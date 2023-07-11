import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_menu_principal import MenuPrincipal
from gui_menu_configuracion import MenuConfiguracion
from gui_menu_niveles import MenuNiveles
from gui_menu_Game_Over import MenuGameOver
from gui_menu_you_won import MenuYouWon
from gui_menu_you_won_L3 import MenuYouWonL3
from gui_menu_pausa import MenuPausa
from gui_menu_nivel1 import FormGameLevel1
from gui_menu_nivel2 import FormGameLevel2
from gui_menu_nivel3 import FormGameLevel3


flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

menu_principal = MenuPrincipal(name="menuPrincipal",master_surface = screen,x=1,y=1,w=ANCHO_VENTANA,h=ALTO_VENTANA,active=True)
menu_configuracion = MenuConfiguracion(name="menuConfiguracion",ruta="",master_surface = screen,x=300,y=200,w=720,h=324,active=False)
menu_niveles = MenuNiveles(name="menuNiveles",master_surface = screen,x=300,y=200,w=864,h=388.8,active=False)
menu_game_over =MenuGameOver(name="menuGameOver",master_surface = screen,x=1,y=1,w=ANCHO_VENTANA,h=ALTO_VENTANA,ruta="",active=False)
menu_you_won =MenuYouWon(name="menuYouWon",master_surface = screen,x=1,y=1,w=ANCHO_VENTANA,h=ALTO_VENTANA,ruta="",active=False)
menu_you_won_L3 =MenuYouWonL3(name="menuYouWonL3",master_surface = screen,x=1,y=1,w=ANCHO_VENTANA,h=ALTO_VENTANA,ruta="",active=False)

menu_pausa =MenuPausa(name="menuPausa",master_surface = screen,x=300,y=200,w=864,h=388.8,ruta="",active=False)


form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,active=False)


while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    print(aux_form_active)

    if menu_pausa.flag:
        menu_configuracion.set_ruta("menuPausa")
    else:
        menu_configuracion.set_ruta("menuPrincipal")

    if form_game_L1.flag:
        menu_pausa.set_ruta("form_game_L1")
        menu_you_won.set_ruta("form_game_L2")
        menu_game_over.set_ruta("form_game_L1")
    elif form_game_L2.flag:
        menu_pausa.set_ruta("form_game_L2")
        menu_you_won.set_ruta("form_game_L3")
        menu_game_over.set_ruta("form_game_L2")
    elif form_game_L3.flag:
        menu_pausa.set_ruta("form_game_L3")
        menu_game_over.set_ruta("form_game_L3")

    if aux_form_active != None:
        aux_form_active.update(lista_eventos, keys, delta_ms)
        aux_form_active.draw()

    pygame.display.flip()
      


  



