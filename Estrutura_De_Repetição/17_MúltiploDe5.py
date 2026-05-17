"""17) - Desenvolva um algoritmo que leia 10 valores e ao final exiba a quantidade de valores múltiplo de 5."""

# continuar = True
# qtd_multiplos = 0
#
# while continuar:
#     valores = int(input("Informe um valor: "))
#     if valores > 5 * 2:
#         qtd_multiplos = qtd_multiplos + 1
#
#     opcao = input("Pressione qualquer tecla para continuar ou informe 'N' para encerrar: ")
#
#     if opcao == "n":
#         continuar = False
# print(f"Quantidade de múltiplos de 5: {qtd_multiplos}")

valores = 10
qtd_multiplos = 0

for n in range(1, valores + 1):
    numeros = int(input("Informe um valor: "))
    if numeros % 5 == 0:
        qtd_multiplos = qtd_multiplos + 1
        print("O Valor informado é múltiplo de 5.")
print(f"Quantidade de múltiplos de 5: {qtd_multiplos}")
