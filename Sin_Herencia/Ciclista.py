# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Ciclista(object):
    def __init__(self, nombre, apellidos, edad, bici, especialidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.bici = bici
        self.especialidad = especialidad

    def entrenar(self, distancia):
        print (self.nombre + ' entrena una distancia de: ' + distancia)

    def competir(self, distancia):
        print (self.nombre + ' compite en una distancia de ' +
               distancia + ' Km')

    def ajustar_bici(self):
        print (self.nombre + ' ajusta la bici')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + self.bici + ' | ' + self.especialidad
