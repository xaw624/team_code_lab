def cuadrado(lista):
    respuesta=[]
    for numerito in lista:
        #print(isinstance(numerito, (int, float)))
        if isinstance(numerito, (int, float)):
            respuesta.append(numerito**2)
        else:
            print(f" este, {numerito}, no es un númerito") 
    return respuesta
        
lista=[1,2,"a",3,"b"]
print (cuadrado(lista))

