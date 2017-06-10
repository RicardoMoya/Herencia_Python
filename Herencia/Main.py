# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from Atleta import Atleta
from Ciclista import Ciclista
from Nadador import Nadador

gebrselassie = Atleta("Haile", "Gebrselassie", 44, ["5 Km", "10 Km",
                                                    "1/2 Maraton", "Maraton"])

indurain = Ciclista("Miguel", "Indurain", 52, "Pinarello", "Contrareloj")

phelps = Nadador("Michael", "Phelps", 31, ["Mariposa", "Espalda",
                                           "Braza", "Crol"])

# Imprimimos los objetos
print (gebrselassie)
print (indurain)
print (phelps)

# Entrenan
print ('\nENTRENAN')
gebrselassie.entrenar("15 Km")
indurain.entrenar("100 Km")
phelps.entrenar("3000 m")

# Compiten
print ('\nCOMPITEN')
gebrselassie.competir("Maraton")
indurain.competir("230 Km")
phelps.competir("400 estilos")

# Método propio
print ('\nHACEN')
gebrselassie.tecnica_carrera()
indurain.ajustar_bici()
phelps.estudiar_tecnica_natacion()
