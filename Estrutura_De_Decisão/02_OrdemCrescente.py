"""2. Faça um algoritmo para ler duas variáveis inteiras A e B e garantir que A e B fiquem em ordem crescente, ou seja,
a variável A deverá armazenar o menor valor fornecido e a variável B o maior"""

A = int(input("Insira um valor para A: "))
B = int(input("Insira um valor para B: "))

if A < B:
    print(f"A={A}, B={B}.")
else:
    C = B
    B = A
    A = C
    print(f"A={A}, B={B}.")
