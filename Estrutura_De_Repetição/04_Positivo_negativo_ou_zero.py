"""04) - Faça um algoritmo que receba "N" números e mostre positivo, negativo, ou zero para cada número."""

qtd_positivo = 0
qtd_negativo = 0
qtd_zeros = 0
continuar = True

while continuar:
    numero = int(input("Informe um número: "))
    if numero > 0:
        print("=========================================")
        print(f"O Número {numero} é positivo.")
        print("=========================================")
        qtd_positivo = qtd_positivo + 1
    elif numero < 0:
        print("=========================================")
        print(f"O Número {numero} é negativo.")
        print("=========================================")
        qtd_negativo = qtd_negativo + 1
    else:
        print("=========================================")
        print("O Número é igual a zero.")
        print("=========================================")
        qtd_zeros = qtd_zeros + 1

    opcao = input("Deseja continuar? [S/N]: ").upper()

    if opcao == "N":
        print("=====================================================")
        print(f"Números positivos informados: {qtd_positivo}")
        print(f"Números negativos informados: {qtd_negativo}")
        print(f"Números igual a zero informados: {qtd_zeros}")
        print("=====================================================")
        continuar = False
