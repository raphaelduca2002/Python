"""4. Escreva um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total
percorrida pelo automóvel e o total de combustível gasto."""


#  Entrada de Dados

distancia = float(input("Informe a distância percorrida pelo automóvel em Quilômetros: "))
combustivel = float(input("Informe a quantidade de combustível gasto em Litros: "))

#  Processamento de Dados

media = distancia / combustivel

#  Saída de Dados

print(f"A Média de combustível gasto foi de: {media:.2f} KM/L")

#  FIM
