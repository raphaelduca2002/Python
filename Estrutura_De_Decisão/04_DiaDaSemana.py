"""4.	Desenvolva um algoritmo que receba o dia da semana (número) e informe o dia da semana (literal).

DIA	DESCRIÇÃO
1	Segunda-Feira
2	Terça-Feira
3	Quarta-Feira
4	Quinta-feira
5	Sexta-Feira
6	Sábado
7	Domingo"""

dia1 = "Segunda-Feira"
dia2 = "Terça-Feira"
dia3 = "Quarta-Feira"
dia4 = "Quinta-Feira"
dia5 = "Sexta-Feira"
dia6 = "Sábado"
dia7 = "Domingo"

numero = int(input("Informe o número de 1 a 7: "))
match numero:
    case 1:
        print(dia1)
    case 2:
        print(dia2)
    case 3:
        print(dia3)
    case 4:
        print(dia4)
    case 5:
        print(dia5)
    case 6:
        print(dia6)
    case 7:
        print(dia7)
    case _:
        print("Número Inválido!")