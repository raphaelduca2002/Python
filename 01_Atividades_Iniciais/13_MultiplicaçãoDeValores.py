"""13. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) O produto do dobro do primeiro com metade do segundo.
b) A soma do triplo do primeiro com o terceiro."""

#  Entrada de Dados

valor1 = int(input("Informe o primeiro valor inteiro: "))
valor2 = int(input("Informe o segundo valor inteiro: "))
valor3 = float(input("Informe o primeiro valor real: "))

#  Processamento de Dados

resposta_a = (2 * valor1) + (valor2 / 2)
resposta_b = (3 * valor1) + valor3

#  Saída de Dados

print(f"O produto do dobro do primeiro com metade do segundo é: {resposta_a}")
print(f"A soma do triplo do primeiro com o terceiro é: {resposta_b}")
