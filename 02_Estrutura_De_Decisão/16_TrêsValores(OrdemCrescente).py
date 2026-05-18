"""16.	Escreva um algoritmo que leia 3 valores inteiros (considere que não serão informados valores iguais)
 e escrevê-los em ordem crescente."""

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print(f"Valor1: {valor1}")
    print(f"Valor2: {valor2}")
    print(f"Valor3: {valor3}")

elif valor2 > valor1 and valor2 > valor3:
    print(f"Valor2: {valor2}")
    print(f"Valor3: {valor3}")
    print(f"Valor1: {valor1}")

elif valor3 > valor1 and valor3 > valor2:
    print(f"Valor3: {valor3}")
    print(f"Valor2: {valor2}")
    print(f"Valor1: {valor1}")

elif valor1 == valor2 == valor3:
    print("Todos os valores são iguais!")