"""11.	Faça um algoritmo para ler dois números inteiros e informar se estes números são iguais ou diferentes.
"""

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

if valor1 == valor2:
    print(f"Os valores informados {valor1} e {valor2} são iguais!")
elif valor1 != valor2:
    print(f"Os valores informados {valor1} e {valor2} são diferentes!")