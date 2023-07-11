import random
import time
from enemigo import Enemy
from objetos_auxiliares import *

class EnemyGenerator:
    def __init__(self, x_range, y_range,gravity,cantidad_enemigos, speed_range, shoot_interval_range,ruta_camina,columnas_camina,puntaje):
        self.x_range = x_range
        self.y_range = y_range
        self.speed_range = speed_range
        self.shoot_interval_range = shoot_interval_range
        self.ruta_camina = ruta_camina
        self.columnas_camina = columnas_camina
        self.gravity = gravity
        self.puntaje = puntaje
        self.score = 0
        self.current_time = 0
        self.finished = False
        self.cantidad_enemigos = cantidad_enemigos

    def generate_enemy(self):
        x = random.randint(*self.x_range)
        y = random.randint(*self.y_range)
        speed_walk = random.uniform(*self.speed_range)
        tiempo_disparo = random.uniform(*self.shoot_interval_range)

        return Enemy(x, y,self.ruta_camina,self.columnas_camina,speed_walk, tiempo_disparo, self.gravity, frame_rate_ms=300, move_rate_ms=100)

    def update(self,delta_ms,enemy_list):
        for enemy in enemy_list:     
            if enemy.muerto:
                self.finished = True
                self.score += self.puntaje
                enemy_list.remove(enemy)
            self.current_time += delta_ms
            if self.current_time >= 5000 and len(enemy_list) < self.cantidad_enemigos:
                new_enemy = self.generate_enemy()
                enemy_list.append(new_enemy)
                self.finished = False
                self.current_time = 0
            if self.finished:
                enemy.explosion.do_animation(delta_ms)


import random

class RocaGenerator:
    def __init__(self, x_range, gravity_range, cantidad_rocas):
        self.x_range = x_range
        self.gravity_range = gravity_range
        self.current_time = 0
        self.cantidad_rocas = cantidad_rocas

    def generate_roca(self):
        x = random.randint(*self.x_range)
        gravity = random.choice(self.gravity_range)

        return Roca(x, 50, gravity)

    def update(self, delta_ms, lista_rocas):
        self.current_time += delta_ms

        if self.current_time >= 3000 and len(lista_rocas) < self.cantidad_rocas:
            new_roca = self.generate_roca()
            lista_rocas.append(new_roca)
            self.current_time = 0

        for roca in lista_rocas:
            if roca.finished:
                lista_rocas.remove(roca)

class TumbaGenerator:
    def __init__(self, tumbas_list_tuplas, tiempo_ataque, cantidad_tumbas):
        self.tumbas_list_tuplas = tumbas_list_tuplas
        self.current_time = 0
        self.cantidad_tumbas = cantidad_tumbas
        self.tiempo_ataque = tiempo_ataque

    def generate_tumba(self):
        tupla_coords = random.choice(self.tumbas_list_tuplas)
        x = tupla_coords[0]
        y = tupla_coords[1]
        lado = random.choice([True, False])

        return Tumba(x, y, self.tiempo_ataque, lado)

    def update(self, delta_ms, lista_tumbas):
        self.current_time += delta_ms

        if self.current_time >= self.tiempo_ataque and len(lista_tumbas) < self.cantidad_tumbas:
            new_tumba = self.generate_tumba()
            lista_tumbas.append(new_tumba)
            self.current_time = 0

        for tumba in lista_tumbas:
            if not tumba.visible:
                lista_tumbas.remove(tumba)