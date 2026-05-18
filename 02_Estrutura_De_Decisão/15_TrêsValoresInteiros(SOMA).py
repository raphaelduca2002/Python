"""15.	Escreva um algoritmo que leia 3 valores inteiros (considere que não serão informados valores iguais)
 e escrever a soma dos 2 maiores."""

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print(valor1)
    valor_final = valor1 + valor2 + valor3
    print(valor_final)
elif valor2 > valor1 and valor2 > valor3:
    print(valor2)
    valor_final = valor1 + valor2 + valor3
    print(valor_final)
elif valor3 > valor1 and valor3 > valor2:
    print(valor3)
    valor_final = valor1 + valor2 + valor3
    print(valor_final)
elif valor1 == valor2 == valor3:
    print("Todos os valores são iguais!")