# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Atleta(object):
    def __init__(self, nombre, apellidos, edad, distancias):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.distancias = distancias

    def entrenar(self, distancia):
        print (self.nombre + ' entrena una distancia de: ' + distancia)

    def competir(self, prueba):
        print (self.nombre + ' compite en la prueba de ' + prueba)

    def tecnica_carrera(self):
        print (self.nombre + ' perfecciona su técnica de carrera')

    def __str__(self):
        return self.nombre + ' ' + self.apellidos + ' | ' + str(self.edad) + \
               ' | ' + str(self.distancias)
