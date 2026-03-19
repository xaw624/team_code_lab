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
        if edad>=10 and edad <20:
            Personas[nombre]["rango_edad"] = "10 a 20"
        elif edad>=1 and edad<10:
            Personas[nombre]["rango_edad"] = "1 a 10"
        elif edad>=30 and edad<40:
            Personas[nombre]["rango_edad"] = "30 a 40"
        elif edad>=20 and edad<30:
            Personas[nombre]["rango_edad"] = "20 a 30"
        elif edad>=40 and edad<50:
            Personas[nombre]["rango_edad"] = "40 a 50"
        else:
            Personas[nombre]["rango_edad"] = "Más de 50"
    return Personas

Personas_clasificadas = Clasificador(Personas)
pprint.pprint(Personas_clasificadas)
