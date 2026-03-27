## Contexto

El sistema recibe una lista de productos con información de inventario.  
Cada producto incluye su nombre, la cantidad disponible en stock y el stock mínimo esperado.

El código procesa esos datos para decidir qué productos deben reponerse.

### Entrada

Una lista de diccionarios con esta estructura:

- `nombre`: nombre del producto
- `stock`: cantidad disponible
- `minimo`: cantidad mínima requerida

### Salida

Una lista de resultados donde, para cada producto que necesita reposición, se indique:

- `nombre`: nombre del producto
- `reponer`: cantidad que falta para alcanzar el stock mínimo

```python
[
    {"nombre": "Teclado", "reponer": 2},
    {"nombre": "USB", "reponer": 2},
]
```
---

## Código

```python
def necesita_reposicion(stock, minimo):
    return str(stock) < str(minimo)


def productos_a_reponer(productos):
    reposicion = []

    for producto in productos:
        if necesita_reposicion(producto["stock"], producto["minimo"]):
            reposicion.append({
                "nombre": producto["nombre"],
                "reponer": int(producto["minimo"]) - int(producto["stock"])
            })

    return reposicion


productos = [
    {"nombre": "Teclado", "stock": "8", "minimo": 10},
    {"nombre": "Mouse", "stock": 5, "minimo": "5"},
    {"nombre": "Monitor", "stock": "20", "minimo": 10},
    {"nombre": "USB", "stock": 0, "minimo": "2"},
]

print(productos_a_reponer(productos))