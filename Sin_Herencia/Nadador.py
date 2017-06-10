# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Nadador(object):
    def __init__(self, nombre, apellidos, edad, estilos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.estilos = estilos

    def entrenar(self, distancia):
        print (self.nombre + ' entrena una distancia de: ' + distancia)

    def competir(self, distancia):
        print (self.nombre + ' compite en ' + distancia)

    def estudiar_tecnica_natacion(self):
        print (self.nombre + ' estudia su tecnica de natación')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + str(self.estilos)
