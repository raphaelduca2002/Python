"""6. Desenvolva um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu
nome, o salário fixo e salário no final do mês."""

#  Entrada de Dados

nome = str(input("Informe o Nome do Vendedor: "))
salario_fixo = float(input("Informe o salário fixo do vendedor: "))
totalvendas = float(input("Informe o total de vendas em dinheiro: "))

#  Processamento de Dados

comissao = (totalvendas * 15) / 100
salariofinal = salario_fixo + comissao

#  Saída de Dados

print(f"O Vendedor: {nome}")
print(f"Tem um salário fixo de: {salario_fixo:.2f} R$")
print(f"Tem um total de vendas em dinheiro de {totalvendas:.2f} R$")
print(f"Recebe 15% de comissão sobre o total de vendas em dinheiro no valor de: {comissao:.2f} R$")
print(f"Receberá ao final do mês o salário final + comissão: {salariofinal:.2f} R$")

