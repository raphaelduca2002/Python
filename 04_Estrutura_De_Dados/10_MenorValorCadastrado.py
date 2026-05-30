"""10) - Desenvolva um programa em python que leia 10 valores inteiros informado pelo usuário.
No final exibir o menor valor cadastrado no vetor.
"""

lista = []

for i in range(10):
    print(f"{i + 1}/10")
    valor = int(input(f"Digite um valor: "))
    lista.append(valor)

print("-" * 60)
print(f"Lista completa: {lista}")
print(f"O menor valor cadastrado: {min(lista)}")