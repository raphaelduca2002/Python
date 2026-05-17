"""2. Desenvolva um algoritmo que receba dois números e ao final exiba a soma, a subtração, a multiplicação e a
divisão dos números lidos."""


# Entrada de dados e Variáveis

texto1 = input("Informe o Primeiro valor: ")  # ESCREVA + LEIA
texto2 = input("Informe o Segundo valor: ")

valor1 = int(texto1)
valor2 = int(texto2)

# Processamento de Dados

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

# Saída de Dados
print("O Resultado da soma é de: ", soma)
print("O Resultado da subtração é de: ", subtracao)
print("O Resultado da multiplicação é de: ", multiplicacao)
print("O Resultado da divisão é de: ", divisao)
#  FIM
