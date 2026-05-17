"""8.	Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior."""

valor1 = int(input("Informe um valor: "))
valor2 = int(input("Informe um segundo valor: "))

if valor1 > valor2:
    print(f"A variável valor1 {valor1} é maior que a variável valor2 {valor2}")
elif valor2 > valor1:
    print(f"A variável valor2 {valor2} é maior que a variável valor1 {valor1}")
elif valor1 == valor2:
    print(f"As variáveis valor1 e valor2 tem o mesmo valor!")
