def agrupar(lista):
    grupos={}
    for palabras in lista:
        #separador.join(iterable)
        # separador = ''.join(palabras)
        separador = ''.join(sorted(palabras))
        if separador not in grupos:
                grupos[separador] = []
        grupos[separador].append(palabras)
        
    return list(grupos)
#Aun no está xdxd