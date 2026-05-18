"""5.	Faça um algoritmo para ler um salário e atualizá-lo de acordo com a tabela abaixo.
FAIXA SALARIAL	AUMENTO
Até 600,00			30%
600,01 a 1.100,00	25%
1100,01 a 2.400,00	20%
2400,01 a 3.550,00	15%
Acima de 3.550,00	10%"""

salario = float(input("Informe o salário: "))

if salario <= 600.00:
          aumento = salario * 30 / 100
          salario_final = salario + aumento
          print(f"{salario_final:.2f} R$, aumento de 30% ({aumento:.2f} R$)")

if 600.01 <= salario <= 1100.00:
          aumento = salario * 25 / 100
          salario_final = salario + aumento
          print(f"{salario_final:.2f} R$, aumento de 25% ({aumento:.2f} R$)")

if 1100.01 <= salario <= 2400.00:
          aumento = salario * 20 / 100
          salario_final = salario + aumento
          print(f"{salario_final:.2f} R$, aumento de 20% ({aumento:.2f} R$)")

if 2400.01 <= salario <= 3550.00:
          aumento = salario * 15 / 100
          salario_final = salario + aumento
          print(f"{salario_final:.2f} R$, aumento de 15% ({aumento:.2f} R$)")

if salario > 3550.00:
          aumento = salario * 10 / 100
          salario_final = salario + aumento
          print(f"{salario_final:.2f} R$, aumento de 10% ({aumento:.2f} R$)")