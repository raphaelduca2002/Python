"""2) - Desenvolva um programa em python que leia 10 valores inteiros e armazeno-os em um vetor.
     a) Construa uma função que recebe como parâmetro o vetor com os valores cadastrados e exiba o valor e o índice
     dos elementos que são pares.

     b) Construa uma função que recebe como parâmetro o vetor com os valores cadastrados e exiba o valor e o Índice
     dos elementos que são ímpares.

     c) Construa uma função que recebe como parâmetro o vetor com os valores cadastrados e retorne a soma dos elementos
     do vetor, armazene o retorno da função em uma variável no programa principal e exiba a soma dos elementos.
"""

def valores_pares(vetor):
    """
    :param vetor: Verificação dos elementos pares no vetor.
    """
    print("Elementos pares.")
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            print(f"Índice: {i} | Valor: {vetor[i]}")

def valores_impares(vetor):
    """
    :param vetor: Verificação dos elementos ímpares no vetor.
    """
    print("Elementos impares")
    for i in range(len(vetor)):
        if vetor[i] % 2 != 0:
            print(f"Índice: {i} | Valor: {vetor[i]}")

def soma_dos_elementos(vetor):
    """
    :param vetor: Operação de soma dos elementos dos vetores pares e ímpares.
    :return: Retorna a soma.
    """
    soma = 0
    for valor in vetor:
        soma += valor
    return soma

def programa_principal():
    valores = []

    print("Informe 10 valores inteiros.")
    for i in range(1 , 11, 1):
        valores.append(int(input(f"Informe o {i}º valor: ")))

    valores_pares(valores)
    valores_impares(valores)

    total = soma_dos_elementos(valores)
    print(f"A soma de todos os elementos no vetor é: {total}")

programa_principal()
