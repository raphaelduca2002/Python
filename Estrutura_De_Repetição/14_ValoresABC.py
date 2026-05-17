"""14) - Dados três valores A, B e C, em que A e B são números reais e C é um caractere,
pede-se para imprimir o resultado da operação de A por B se C for um símbolo de operador aritmético;
caso contrário deve ser impressa uma mensagem de operador não definido.
Tratar erro de divisão por zero. Repita esse processo cinco vezes."""


operacoes = 5

for i in range(1, operacoes + 1):
    print(f"Operação: {i}/5")
    try:
        A = int(input("Informe um numero inteiro: "))

        B = int(input("Informe um numero inteiro: "))

        C = input("Informe um caractere aritmético: ")
    except ValueError:
        print("Tente novamente.")
        continue

    match C:
        case "+":
            numero = A + B
            print(f"O Resultado da soma é: {numero} ({A} + {B})")
        case "-":
            numero = A - B
            print(f"o Resultado da subtração é: {numero} ({A} - {B})")
        case "*":
            numero = A * B
            print(f"o Resultado da multiplicação é: {numero} ({A} * {B})")
        case "/": # Como transformar as variáveis A e B em float?
            try:
                numero = A // B
                print(f"o Resultado da divisão é: {numero} ({A} / {B})") # Como imprimir o maior valor no resultado?
            except ZeroDivisionError:
                print("Não é possível dividir por zero, tente novamente.")
        case _:
            print("Caractere inválido, tente novamente.")

input("Fim da operação.")

