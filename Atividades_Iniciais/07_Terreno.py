"""7. Desenvolva um algoritmo que receba como entrada as medidas de um terreno e calcule e exiba sua área do terreno."""

#  Entrada de Dados

largura = float(input("Informe a largura do terreno em metros: "))
profundidade = float(input("Informe a profundidade do terreno em metros: "))

#  Processamento de Dados

area = largura * profundidade

#  Saída de Dados

print(f"A área total do terreno é de: {area} M²")
