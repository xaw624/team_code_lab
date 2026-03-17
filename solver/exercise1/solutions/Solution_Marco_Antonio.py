
def cuadrado(a):
    print(type(a))
    if type(a)==bool:
        return print("la funcion no admite varibles logicas")
    else:
        return a*a

    
lista=[3, 4.678, 4, 5,"AAA"]
lista_final = []
for elemento in lista:
    resultado=cuadrado(elemento)
    lista_final.append(resultado)
    
print(lista_final)