"""10. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que
receba um valor de uma compra e mostre o valor das prestações."""

#  Entrada de Dados

produto = float(input("Informe o valor do produto: "))
prestacao = int(input("Informe a quantidade de prestações: "))

#  Processamento de Dados

valorprestacao = produto / prestacao

#  Saída de Dados

print(f"O Valor do produto é de: {produto:.2f} R$")
print(f"A Quantidade de prestações é de: {prestacao}")
print(f"O Valor das prestações é de: {valorprestacao:.2f} R$")
