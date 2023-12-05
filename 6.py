codigo: str = "4921-AB"

codigo_separado: list = codigo.split("-")

primera_parte: str = codigo_separado[0]
segunda_parte: str = codigo_separado[1]

correcto: bool = False
if (len(primera_parte) == 4):
    if (len(segunda_parte) == 2):
        if (primera_parte.isdigit() == True):
            if (segunda_parte.isdigit() == False):
                contador: int = 0
                for i in segunda_parte:
                    if (i.isdigit() == False):
                        contador+=1
                if (contador == 2):
                    correcto = True

print(correcto)