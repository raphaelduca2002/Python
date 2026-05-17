"""16) - Faça um algoritmo que calcule o valor da conta de luz de 30 pessoas. Sabe-se que o cálculo da conta de luz segue a tabela abaixo:
      Tipo de Cliente		Valor do KW/h
      1 (Residência)		R$ 0,60
      2 (Comércio)			R$ 0,48
      3 (Indústria)			R$ 1,29"""

conta_de_luz = 30

print("------------------------------CONTAS-DE-LUZ------------------------------")

for conta in range(1, conta_de_luz + 1):

    print(f"Conta {conta}")
    tipo = int(input("Informe o tipo do cliente (1 Residência, 2 Comércio, 3 Indústria): "))

    match tipo:
        case 1:
            print("=" * 60)
            print("Tipo do cliente 1 (Residência) Valor do KW/h = R$ 0,60")
            valor_kwh = 0.60
            valor_dia = valor_kwh * 24
            valor_mes = valor_dia * 30
            print(f"Valor do KW/h por dia = {valor_dia:.2f} R$")
            print(f"Valor do KW/h por mes = {valor_mes:.2f} R$")
            print(f"Valor total a pagar da conta de luz ao mês = R$ {valor_mes:.2f} R$")
            print("=" * 60)
        case 2:
            print("=" * 60)
            print("Tipo do cliente 2 (Comércio) Valor do KW/h = R$ 0,48")
            valor_kwh = 0.48
            valor_dia = valor_kwh * 24
            valor_mes = valor_dia * 30
            print(f"Valor do KW/h por dia = {valor_dia:.2f} R$")
            print(f"Valor do KW/h por mes = {valor_mes:.2f} R$")
            print(f"Valor total a pagar da conta de luz ao mês = R$ {valor_mes:.2f} R$")
            print("=" * 60)
        case 3:
            print("=" * 60)
            print("Tipo do cliente 3 (Indústria) Valor do KW/h = R$ 1,29")
            valor_kwh = 1.29
            valor_dia = valor_kwh * 24
            valor_mes = valor_dia * 30
            print(f"Valor do KW/h por dia = {valor_dia:.2f} R$")
            print(f"Valor do KW/h por mes = {valor_mes:.2f} R$")
            print(f"Valor total a pagar da conta de luz ao mês = R$ {valor_mes:.2f} R$")
            print("=" * 60)
        case _:
            print("=" * 60)
            print("Tipo inválido, tente novamente")
            print("=" * 60)
