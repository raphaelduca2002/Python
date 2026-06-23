"""4) - Leia valores e armazene em um vetor. Crie as funções abaixo que receba como parâmetro o vetor lido e exiba:
     a) - A soma dos elementos do vetor.
     b) - O maior elemento cadastrado no vetor.
     c) - O menor elemento cadastrado no vetor.
     d) - O número de ocorrências do primeiro elemento.
     e) - A média dos elementos.
     f) - A quantidade de elementos pares.
     g) - A quantidade de elementos Ímpares.
     f) - A soma dos elementos pares.
     h) - A soma dos elementos Ímpares."""

def soma_dos_elementos(vetor):
    """
    :param vetor: Operação de soma dos elementos dos vetores pares e ímpares.
    :return: Retorna a soma.
    """
    soma = 0
    for valor in vetor:
        soma += valor
    return soma

def maior_elemento(vetor):
    """
    :param vetor: Buscar o maior elemento cadastrado no vetor.
    :return: Retorna o maior elemento.
    """
    maior_valor = 0
    for valor in vetor:
        if valor > maior_valor:
            maior_valor = valor
    return maior_valor

def menor_elemento(vetor):
    """
    :param vetor: Buscar o menor elemento cadastrado no vetor.
    :return: Retorna o menor elemento.
    """
    menor_valor = vetor[0]
    for valor in vetor:
        if valor < menor_valor:
            menor_valor = valor
    return menor_valor

def ocorrencias_do_primeiro_elemento(vetor):
     """
    :param vetor: Contar as ocorrências do primeiro elemento no vetor.
    :return: Número de vezes que o primeiro elemento se repete.
    """
    if not vetor:
        return 0
    return vetor.count(vetor[0])

def media_dos_elementos(vetor):
    """
    :param vetor: Determinar a média dos elementos no vetor.
    :return: Média dos elementos.
    """
    media = 0
    for valor in vetor:
        media += valor
    return media/len(vetor)

def qtd_pares(vetor):
    """
    :param vetor: Contador para determinar a quantidade de elementos que são pares.
    :return: Quantidade de elementos pares.
    """
    qtd = 0
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            qtd += 1
    return qtd

def qtd_impares(vetor):
    """
    :param vetor: Contador para determinar a quantidade de elementos que são ímpares.
    :return: Quantidade de elementos ímpares.
    """
    qtd = 0
    for i in range(len(vetor)):
        if vetor[i] % 2 != 0:
            qtd += 1
    return qtd

def soma_pares(vetor):
    """
    :param vetor: Função para realizar a soma dos elementos pares.
    :return: Soma dos elementos pares.
    """
    soma = 0
    for valor in vetor:
        if valor % 2 == 0:
            soma += valor
    return soma

def soma_impares(vetor):
    """
    :param vetor: Função para realizar a soma dos elementos ímpares.
    :return: Soma dos elementos ímpares.
    """
    soma = 0
    for valor in vetor:
        if valor % 2 != 0:
            soma += valor
    return soma

def programa_principal():
    valores = []

    print("Informe 10 valores inteiros.")
    for i in range(1, 11, 1):
        valores.append(int(input(f"Informe o {i}º valor: ")))
        # valores.append(i)

    print("-" * 45)
    print(f"Soma de todos os elementos no vetor: {soma_dos_elementos(valores)}")
    print(f"Maior elemento do vetor: {maior_elemento(valores)}")
    print(f"Menor elemento do vetor: {menor_elemento(valores)}")
    print(f"Ocorrências de valores que se repetem com o primeiro elemento: {ocorrencias_do_primeiro_elemento(valores)}")
    print(f"Média dos valores: {media_dos_elementos(valores)}")
    print(f"Quantidade de elementos pares: {qtd_pares(valores)}")
    print(f"Quantidade de elementos ímpares: {qtd_impares(valores)}")
    print(f"Soma dos valores pares: {soma_pares(valores)}")
    print(f"Soma dos valores ímpares: {soma_impares(valores)}")

programa_principal()

