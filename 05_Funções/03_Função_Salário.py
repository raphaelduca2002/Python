"""3) - Desenvolva um programa em python, que leia o salário de 10 funcionários.
Crie uma função para calcular o novo salário do funcionário que recebera aumento de 15%.
Exiba o novo salário dos funcionários."""

def aumento(salario):
    """
    :param salario: Calcular o aumento do salário em 15%.
    :return: Retornar o aumento.
    """
    return salario * 1.15

def programa_principal():

    salario_dos_funcionarios = []

    for i in range (1, 11, 1):

        salario = float(input(f"Informe o salário do funcionário {i}: "))

        salario_dos_funcionarios.append(salario)

        print("----------Sistema de verificação de aumento de salário----------")

        for x, salario in enumerate(salario_dos_funcionarios, + 1):

            novo_salario = aumento(salario)

            print(f"Funcionário {x}: Salário Antigo R$ {salario:.2f} | Novo Salário R$ {novo_salario:.2f} aumento de 15%")


programa_principal()
