"""6) - Desenvolva um programa em python que leia valores inteiros e armazene-os em um vetor, calcule e exiba as seguintes informações:
   a) - A quantidade de números pares.
   b) - Os números pares.
   c) - A quantidade de números ímpares.
   d) - Os valores ímpares.
   e) - A média dos valores pares.
   f) - A média dos valores ímpares.
   g) - A média da soma dos valores pares mais os valores ímpares."""

vetor = []
contador = 1
qtdPar = 0
qtdImpar = 0
media_par = 0
media_impar = 0
media_soma = 0

for x in range(1, 11, 1):
    print(f"({x}/10)")
    vetor.append(int(input(f"Informe o {x}º valor: ")))

print("-" * 30)

for numeros in vetor:
    if numeros % 2 == 0:
        print(f"{contador} - {numeros} Par")
        contador += 1
        qtdPar += 1
        media_par = qtdPar / 2
    else:
        print(f"{contador} - {numeros} Ímpar")
        contador += 1
        qtdImpar += 1
        media_impar = qtdImpar / 2

media_soma = media_par + media_impar

print("-" * 30)
print(vetor)
print("-" * 30)
print(f"Quantidade de números pares: {qtdPar}")
print(f"Quantidade de números ímpares: {qtdImpar}")
print(f"Média dos números pares: {media_par}")
print(f"Média dos números ímpares: {media_impar}")
print(f"A média da soma dos valores pares mais os valores ímpares: {media_soma}")