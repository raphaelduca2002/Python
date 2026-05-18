"""11. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de
custo receberá um acréscimo de acordo com um percentual informado pelo usuário."""

#  Entrada de Dados

preco_custo = float(input("Informe o preço de custo do produto: "))
percentual = float(input("Informe o percentual de aumento do produto: "))

#  Processamento de Dados

aumento = (preco_custo * percentual) / 100
preco_venda = preco_custo + aumento

#  Saída de Dados

print(f"O Valor do produto é de : {preco_venda:.2f} R$")
print(f"O Percentual de aumento é de: {percentual:.1f} %")
