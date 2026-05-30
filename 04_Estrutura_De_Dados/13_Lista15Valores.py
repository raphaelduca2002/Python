"""13) - Desenvolva um programa em python que leia 15 valores informados pelo usuário e cadastre-os em uma lista.
 O usuário deverá informar um valor a ser procurado no vetor, caso encontre este valor exiba o índice desse elemento.
"""

lista = []

for i in range(15):
    valor = int(input(f"{i + 1}/15 Informe um valor valor: "))
    lista.append(valor)

print("---------Lista de valores cadastrados---------")
print(lista)

procurar = int(input(f"Informe o valor da lista a ser procurado: "))

if procurar in lista:
    indice = [i for i, valor in enumerate(lista) if valor == procurar]
    print(f"O valor informado ({procurar}) está presente nos índices: {indice} da lista.")
else:
    print("O Valor informado não foi cadastrado na lista")

input("Pressione qualquer tecla para sair...")