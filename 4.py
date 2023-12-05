lista: list = [5, 3, 7, 1, 9, 12, 1, 3, 1]

lista.sort()

listaLimpia: list = []
for i, numero in enumerate(lista):
    actual: int = lista[i]
    siguiente: int = None
    try:    
        siguiente = lista[i + 1]
    except:
        siguiente = None
    
    if (actual != siguiente):
        listaLimpia.append(numero)
    
print(listaLimpia)