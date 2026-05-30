"""5) - Desenvolva um programa em python que leia 30 valores inteiros e armazene-os em um vetor. Exiba os valores do vetor
ao contrário da ordem de leitura dos valores."""

vetor = []
import random

for i in range(1, 31):
    # print(f"{i}/30")
    # vetor.append(int(input("Digite um valor: ")))
    vetor.append(random.randint(10, 99))
print("Vetor Normal:")
print(vetor)
print("Vetor Invertido:")
indice = 29

while indice >= 0:
    print(vetor[indice], end=", ")
    indice = indice - 1
