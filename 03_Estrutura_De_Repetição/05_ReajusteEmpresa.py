"""05) - Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os
seguintes critérios: a) 50% para aqueles que ganham menos do que três salários mínimos; b) 20% para aqueles que
ganham entre três até dez salários mínimos; c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
d) 10% para os demais funcionários. Leia o nome do funcionário, seu salário e o valor do salário mínimo. Calcule o
seu novo salário reajustado. Escrever o nome do funcionário, o reajuste e seu novo salário. Calcule quanto à empresa
vai aumentar sua folha de pagamento."""

continuar = True
operacoes = 0

print("-" * 25)
print("--- REAJUSTE SALARIAL ---")
print("-" * 25)

salario_minimo = float(input("Informe o salário mínimo atual: "))

while continuar:

    funcionario = input("Informe o nome do funcionário: ")
    salario = float(input(f"Informe o salário do funcionario '{funcionario}': "))

    if salario <= salario_minimo * 3:
        aumento = salario * 0.50  # 50%
        salario_final = salario + aumento
        print("-" * 30)
        print(f"Salário reajustado: {salario_final:.2f} R$")
        print(f"Aumento de: {aumento:.2f} R$ (50% a mais)")
        print("-" * 30)
    elif (3 * salario_minimo) <= salario <= (10 * salario_minimo):
        aumento = salario * 0.20  # 20%
        salario_final = salario + aumento
        print("-" * 30)
        print(f"Salário reajustado: {salario_final:.2f} R$")
        print(f"Aumento de: {aumento:.2f} R$ (20% a mais)")
        print("-" * 30)
    elif (10 * salario_minimo) <= salario <= (20 * salario_minimo):
        aumento = salario * 0.15  # 15%
        salario_final = salario + aumento
        print("-" * 30)
        print(f"Salário reajustado: {salario_final:.2f} R$")
        print(f"Aumento de: {aumento:.2f} R$ (15% a mais)")
        print("-" * 30)
    elif salario >= salario_minimo:
        aumento = salario * 0.10  # 10%
        salario_final = salario + aumento
        print("-" * 30)
        print(f"Salário reajustado: {salario_final:.2f} R$")
        print(f"Aumento de: {aumento:.2f} R$ (10% a mais)")
        print("-" * 30)

    operacoes = operacoes + 1

    print(f"Funcionário {operacoes} cadastrado.")
    opcao = input("Deseja continuar? [S/N]: ").upper()

    if opcao == "N":
        print("Fim da operação.")
        print(f"Quantidade de operações de reajuste: {operacoes}")
        input("Pressione qualquer tecla para encerrar.")
        continuar = False
