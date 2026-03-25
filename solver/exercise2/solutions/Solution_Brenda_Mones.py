# def agrupar(lista):
#     grupos={}
#     for palabras in lista:
#         #separador.join(iterable)
#         # separador = ''.join(palabras)
#         separador = ''.join(sorted(palabras))
#         if separador not in grupos:
#                 grupos[separador] = []
#         grupos[separador].append(palabras)
        
#     return list(grupos)
# #Aun no está xdxd
def contar_letras(palabra):
    conteo = {}
    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1    
    return conteo
def anagramas(p1, p2):
    return contar_letras(p1) == contar_letras(p2)
def agrupar_anagramas(lista):
    grupos = []
    usados = [False] * len(lista)
    return grupos

letritas = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(agrupar_anagramas(letritas))