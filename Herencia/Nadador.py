# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from Deportista import Deportista

class Nadador(Deportista):
    def __init__(self, nombre, apellidos, edad, estilos):
        Deportista.__init__(self, nombre, apellidos, edad)
        self.estilos = estilos

    def estudiar_tecnica_natacion(self):
        print (self.nombre + ' estudia su tecnica de natación')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + str(self.estilos)
