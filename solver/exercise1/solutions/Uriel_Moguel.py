def lista_cuadrado(lista:list):
    lista_destino  = []
    errores = []
    for elemento in lista:
        try:
            cuadrado  = elemento**2     
            lista_destino.append(cuadrado)
        except Exception as e:
            errores.append(e)
            
    return lista_destino,errores
    
lista=[1,2,True,3,"b"]
print(False & True)
#lista_destino,_ = lista_cuadrado(lista)
#print(lista_destino)
