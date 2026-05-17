"""7.	Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 10."""

valor = int(input("Informe um valor: "))

if valor > 10:
    print(f"O Valor {valor} é maior que 10.")
elif valor < 10:
    print(f"O Valor {valor} é menor que 10.")
elif valor == 10:
    print(f"O Valor {valor} é igual a 10.")
