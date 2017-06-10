# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Deportista(object):
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def entrenar(self, distancia):
        print (self.nombre + ' entrena una distancia de: ' + distancia)

    def competir(self, prueba):
        print (self.nombre + ' compite en la prueba de ' + prueba)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad)
