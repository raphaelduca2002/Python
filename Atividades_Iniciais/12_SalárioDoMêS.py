"""12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
mostre o total do seu salário no referido mês."""

#  Entrada de Dados

valor_hora = float(input("Informe o valor da hora trabalhada: "))
quantidade_hora = float(input("Informe a quantidade de horas trabalhadas no mês: "))

#  Processamento de Dados

salario = valor_hora * quantidade_hora

#  Saída de Dados

print(f"O Seu salário do mês é de: {salario:.2f} R$")
