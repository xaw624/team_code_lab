from numbers import Number

def elevar_al_cuadrado(lista):
    if not isinstance(lista, list):
        raise TypeError("La entrada debe ser una lista.")

    nueva_lista = []
    
    for i, elemento in enumerate(lista):
        if not isinstance(elemento, Number) or isinstance(elemento, bool):
            raise ValueError(f"El elemento en la posición {i+1} no es un número válido: {elemento}")
        
        nueva_lista.append(elemento ** 2) # type: ignore
    
    return nueva_lista



print(elevar_al_cuadrado([1, 2, "3", 4]))
# ValueError: El elemento en la posición 2 no es un número válido: 3