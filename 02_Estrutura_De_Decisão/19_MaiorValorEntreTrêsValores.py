"""19.	Desenvolva um algoritmo que leia três valores inteiro informado pelo usuário
 e ao final exiba o maior valor entre eles."""

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print(f"o maior valor é {valor1}")
elif valor2 > valor1 and valor2 > valor3:
    print(f"o maior valor é {valor2}")
elif valor3 > valor1 and valor3 > valor2:
    print(f"o maior valor é {valor3}")
elif valor1 == valor2 == valor3:
    print("Todos os valores são iguais!")


