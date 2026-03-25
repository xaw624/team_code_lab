lista = ["tea","eat", "tan", "ate", "nat", "bat"]


def agrupar_anagramas(lista: list[str]):
    lista_aux = []
    lista_agrupados = []
    
    while len(lista)>0:
        palabra_comparar = lista[0]
        letras_comparar = set(palabra_comparar)
        for palabra in lista:
            letras = set(palabra)

            if letras== letras_comparar:
                lista_aux.append(palabra)
                
        lista = [ i for i in lista if i not in lista_aux]
        lista_agrupados.append(lista_aux)
        lista_aux=[]
    return lista_agrupados

print(lista)
lista_agrupada = agrupar_anagramas(lista)
print(lista_agrupada)
