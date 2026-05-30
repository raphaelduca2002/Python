"""4) - Desenvolva um programa em python que leia valores inteiros para o vetor A e construa outro vetor B da seguinte forma:
VETOR - A [3, 8, 4, 2, ..., 10]
VETOR - B [9, 4, 12, 1, ..., 5]"""

vetor_A = []
vetor_B = []
indice = 0

print("-" * 60)
print("Você está no vetor A")
while True:
    try:
        vetor_A.append(int(input("Insira um valor para o vetor A: ")))
    except ValueError:
        print("Dados inválidos, tente novamente")
        continue
    opcao = input(
        "Pressione qualquer tecla para continuar inserindo valores no vetor A ou N para encerrar a operação: ")
    if opcao.upper() == "N":
        break

while indice < len(vetor_A):
    if indice % 2 == 0:
        vetor_B.append(vetor_A[indice] * 3)
    else:
        vetor_B.append(vetor_A[indice] / 2)

    indice = indice + 1

# for x in vetor_A:
#     vetor_B.append(x ** 2)

print("-" * 60)
print(f"Construção do vetor A: {vetor_A}")
print(f"Construção do vetor B: {vetor_B}")
print("-" * 60)

