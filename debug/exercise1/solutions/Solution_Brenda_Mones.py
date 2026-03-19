import random
import pprint
Personas = {
    "Juan":    { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"David":   { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Marco":   { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Yeshua":  { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Martin":  { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Vanesa":  { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Segio":   { "Edad" : random.randint(1, 60),  "rango_edad" : None},
	"Eduardo": { "Edad" : random.randint(1, 60),  "rango_edad" : None}
    }

def Clasificador(Personas: dict):
    for nombre in Personas.keys():
        edad = Personas[nombre]["Edad"]
        if edad>=1 and edad <=9:
            Personas[nombre]["rango_edad"] = "1 a 9"
        elif edad >=10 and edad <=19:
            Personas[nombre]["rango_edad"]="10 a 19"
        elif edad>=20 and edad <=29:
            Personas[nombre]["rango_edad"] = "20 a 29"
        elif edad>=30 and edad <=39:
            Personas[nombre]["rango_edad"] = "30 a 39"
        elif edad>=40 and edad <=50:
            Personas[nombre]["rango_edad"] = "40 a 50"
        else:
            Personas[nombre]["rango_edad"] = "Más de 50"
    return Personas


def Clasificador2(Personas: dict):
    for nombre in Personas.keys():
        edad = Personas[nombre]["Edad"]
        if edad<=9:
            Personas[nombre]["rango_edad"] = "1 a 9"
        elif edad<= 19:
            Personas[nombre]["rango_edad"]="10 a 19"
        elif edad <=29:
            Personas[nombre]["rango_edad"] = "20 a 29"
        elif edad <=39:
            Personas[nombre]["rango_edad"] = "30 a 39"
        elif edad <=50:
            Personas[nombre]["rango_edad"] = "40 a 50"
        else:
            Personas[nombre]["rango_edad"] = "Más de 50"
    return Personas

Personas_clasificadas = Clasificador2(Personas)
pprint.pprint(Personas_clasificadas)