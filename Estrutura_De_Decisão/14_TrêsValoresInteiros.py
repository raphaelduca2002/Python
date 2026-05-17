"""14.	Escreva um algoritmo que leia 3 valores inteiros (considere que não serão informados valores iguais)
 e escrever o maior deles."""

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print(valor1)
elif valor2 > valor1 and valor2 > valor3:
    print(valor2)
elif valor3 > valor1 and valor3 > valor2:
    print(valor3)
elif valor1 == valor2 == valor3:
    print("Todos os valores são iguais!")