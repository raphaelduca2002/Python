"""18.	Escreva um algoritmo que leia dois valores inteiros e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.
"""

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 == valor2:
    print("Valores iguais!")
elif valor1 > valor2:
    print("o Primeiro valor é o maior")
elif valor1 < valor2:
    print("o Segundo valor é o maior")