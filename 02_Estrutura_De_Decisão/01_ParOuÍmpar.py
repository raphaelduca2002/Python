"""1. Faça um algorítmo para ler um número inteiro e informar se este número é par ou ímpar"""

numero = int(input("Informe o numero: "))
resto = numero % 2

if resto == 0:
    print(f"O Número {numero} é Par.")
else:
    print(f"O Número {numero} é Ímpar.")


# % --> Mod
# // --> Div

# resto = 10 % 2
# div = 10 // 2
# print(resto)
# print(div)
