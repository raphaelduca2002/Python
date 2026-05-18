"""18) - Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os lados de um triângulo.
Se for, informar qual o tipo de triângulo que eles formam: equilátero, isóscele ou escaleno. Propriedade: o
comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados. Triângulo
Equilátero: aquele que tem os comprimentos dos três lados iguais; Triângulo Isóscele: aquele que tem os comprimentos
de dois lados iguais. Portanto, todo triângulo equilátero é também isóscele; Triângulo Escaleno: aquele que tem os
comprimentos de seus três lados diferentes. Repita esse processo 5 vezes."""

operacoes = 5

print("-" * 10 + "VERIFICAÇÃO DE TRIÂNGULOS" + "-" * 10)

# Laço de repetição de operações:
for n in range(1, operacoes + 1):
    print(f"Triângulo {n}/5: ")

    # Entrada de dados de números inteiros:

    lado1 = int(input("Informe o comprimento do lado 1: CM "))
    lado2 = int(input("Informe o comprimento do lado 2: CM "))
    lado3 = int(input("Informe o comprimento do lado 3: CM "))

    # Verificar se os comprimentos informados podem formar um triângulo:

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3:
        print("-" * 90)
        print("Os comprimentos informados podem formar um triângulo.")
        print("-" * 90)

    # Verificar a classificação do triângulo:

        if lado1 == lado2 == lado3:
            print("Triângulo Equilátero. (3 Lados iguais)")
            print("Triângulo Isóscele. (2 Lados iguais)")
            print("-" * 90)
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triângulo Isóscele. (2 Lados iguais)")
            print("-" * 90)
        else:
            print("Triângulo Escaleno. (3 Lados diferentes)")
            print("-" * 90)

    else:
        print("-" * 90)
        print("Os valores informados não podem formar um triângulo.")
        print("-" * 90)
