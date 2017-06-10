# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from Deportista import Deportista

class Atleta(Deportista):
    def __init__(self, nombre, apellidos, edad, distancias):
        Deportista.__init__(self, nombre, apellidos, edad)
        self.distancias = distancias

    def tecnica_carrera(self):
        print (self.nombre + ' perfecciona su técnica de carrera')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + str(self.distancias)
