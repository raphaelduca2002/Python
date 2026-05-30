"""1) - Desenvolva um programa em python que receba 10 valores informados pelo usuário, armazene-os em um vetor,
depois exiba os dados do vetor."""

vetor = []

# continuar = True

# while continuar:
#     valor = int(input("Informe um valor: "))
#     vetor.append(valor)
#     opcao = input("Pressione qualquer tecla para continuar ou N para encerrar a operação. ")
#     if opcao.upper() == "N":
#         continuar = False
# print(vetor)

for x in range(1, 11, 1):
    print(f"Operação {x}/10")
    valor = int(input("Informe um valor: "))
    vetor.append(valor)
print(vetor)
