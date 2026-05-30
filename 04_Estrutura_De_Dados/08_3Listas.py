"""8) - Desenvolva um programa em python que receba 10 valores numéricos e guarde-os em uma lista.
Verifique se os valores cadastrados são pares ou ímpares e cadastre os valores pares em uma nova lista
e os ímpares em outra lista. No final exibir o conteúdo das três listas."""

lista_par = []
lista_impar = []
lista_completa = []

for x in range(1, 11, 1):
    print(f"({x}/10)")
    valor = int(input(f"Informe o {x}º valor: "))
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

    lista_completa.append(valor)

print("-" * 30)
print("Lista de números pares:")
print(lista_par)
print("Lista de números ímpares:")
print(lista_impar)
print("Lista completa:")
print(lista_completa)
input("Pressione qualquer tecla para sair")
