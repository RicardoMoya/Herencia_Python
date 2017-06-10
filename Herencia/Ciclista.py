# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from Deportista import Deportista

class Ciclista(Deportista):
    def __init__(self, nombre, apellidos, edad, bici, especialidad):
        Deportista.__init__(self, nombre, apellidos, edad)
        self.bici = bici
        self.especialidad = especialidad

    def ajustar_bici(self):
        print (self.nombre + ' ajusta la bici')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + self.bici + ' | ' + self.especialidad
