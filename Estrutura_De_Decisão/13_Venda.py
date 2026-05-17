"""13.	Faça um algoritmo que receba o valor da venda informado pelo usuário, e exiba o valor da compra de acordo com
as condições de pagamento listadas abaixo:
1 - Venda a Vista - desconto de 10%
2 - Venda a Prazo 30 dias - desconto de 5%
3 - Venda a Prazo 60 dias - mesmo preço
4 - Venda a Prazo 90 dias - acréscimo de 5%
5 - Venda com cartão de débito - desconto de 8%
6 - Venda com cartão de crédito - desconto de 7%"""

valor_venda = float(input("Informe o valor em R$ da venda: "))
prazo = input("Informe o prazo de pagamento ou forma de pagamento (Cartão de crédito/débito): ")

match prazo:

    case "A Vista":
        desconto = valor_venda * 10 / 100
        compra = valor_venda - desconto
        print(f"O Valor da compra a vista é de {compra:.2f} (desconto de 10%, {desconto:.2f} R$).")

    case "30 dias":
        desconto = valor_venda * 5 / 100
        compra = valor_venda - desconto
        print(f"O Valor da compra com prazo de 30 dias é de {compra:.2f} R$ (desconto de 5%, {desconto:.2f} R$).")

    case "60 dias":
        print(f"{valor_venda:.2f} R$ mesmo preço.")

    case "90 dias":
        acrescimo = valor_venda * 5 / 100
        compra = valor_venda + acrescimo
        print(f"O Valor da compra com prazo de 90 dias é de {compra:.2f} R$ (acréscimo de 5%, {acrescimo:.2f} R$).")

    case "Cartão de débito":
        desconto = valor_venda * 8 / 100
        compra = valor_venda - desconto
        print(f"O Valor da compra com cartão de débito é de {compra:.2f} R$ (desconto de 8%, {desconto:.2f} R$).")

    case "Cartão de crédito":
        desconto = valor_venda * 7 / 100
        compra = valor_venda - desconto
        print(f"O Valor da compra com cartão de crédito é de {compra:.2f} R$ (desconto de 7%, {desconto:.2f} R$).")







