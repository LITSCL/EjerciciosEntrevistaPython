palabra: str = "arenera"
palabra_lista: list = []

for i in palabra:
    palabra_lista.append(i)

palindroma: bool = True
for i, letra in enumerate(palabra_lista):
    if (palabra_lista[i] != palabra_lista[len(palabra_lista) - 1 - i]):
        palindroma = False
        break

print(palindroma)