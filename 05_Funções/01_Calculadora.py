"""1) - Desenvolva uma calculadora que receba dois valores e a operação a ser executada [+, -, *, /] da seguinte forma:
     - Crie uma função que exibirá o menu da calculadora para o usuário exemplo:
       =====CALCULADORA=====
       = 1 - Somar         =
       = 2 - Subtrair      =
       = 3 - multiplicar   =
       = 4 - Dividir       =
       = 5 - Sair          =
       =====================

- O algoritmo deverá ler os dados informados pelo usuário.
- Crie uma função que receba com parâmetro os valores e a operação a ser executada e retorne o resultado para o
programa principal. Exiba o valor da operação para o usuário."""

def menu():
    """
    :return: Menu
    """
    print('='*10 + 'Calculadora' + '='*10)
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Sair')
    print('='*31)

def calcular(v1: int, v2: int, operacao: str):
    """
    :param v1: Primeiro valor a ser calculado.
    :param v2: Segundo valor a ser calculado.
    :param operacao: Operação a ser realizada.
    :return: Retornar o resultado da operação.
    """

    if operacao == '+':
        return v1 + v2
    elif operacao == '-':
        return v1 - v2
    elif operacao == '*':
        return v1 * v2
    elif operacao == '/':
        if v2 == 0:
            return "Erro: Divisão por zero!"
        return v1 / v2
    else:
        return "Operação inválida"

while True:
    menu()
    escolha = input("Escolha a operação a ser executada: ")
    if escolha == '5':
        input("Encerrando a calculadora...")
        break

    operacoes = {'1': '+', '2': '-', '3': '*', '4': '/'}

    if escolha in operacoes:
        op = operacoes[escolha]

        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))

        resultado = calcular(valor1, valor2, op)

        print(f"Resultado: {valor1} {op} {valor2} = {resultado}")
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 5.")

