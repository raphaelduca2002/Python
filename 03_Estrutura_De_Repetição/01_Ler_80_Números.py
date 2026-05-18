"""01) - Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive)
e 150 (inclusive)"""

import random

contador = 1
qtd_numeros_intervalo = 0
while contador <= 8:
    numero = int(input(f"Informe o {contador}° número: "))
    if numero >= 10:
        if numero <= 150:
            qtd_numeros_intervalo = qtd_numeros_intervalo + 1
    contador = contador + 1  # acumulador

print(f"Achei {qtd_numeros_intervalo} números no intervalo.")
