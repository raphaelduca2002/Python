"""9. Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$)
 O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.
"""

#  Entrada de Dados

dolar = float(input("Informe o valor em Dólar: "))
cotacao = float(input("Informe a cotação do Dólar atual: "))

#  Processamento de Dados

real = dolar * cotacao

#  Saída de Dados

print(f"O Valor em real é de: {real:.2f} R$")
