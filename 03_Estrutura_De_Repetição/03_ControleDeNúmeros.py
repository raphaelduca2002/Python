"""03) - Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 80,
menor que 25 ou igual a 40. O usuário deverá informar se deseja continuar informando os valores."""

continuar = True

while continuar:

    numero = int(input("Informe um número: "))
    if numero > 80:
        print(f"O Número {numero} é maior que 80.")
    elif numero < 25:
        print(f"O Número {numero} é menor que 25.")
    elif numero == 40:
        print(f"O Número {numero} é igual a 40.")

    opcao = input("Digite N para sair ou qualquer tecla para continuar a operação: ")
    if opcao.lower() == "n":
        continuar = False
