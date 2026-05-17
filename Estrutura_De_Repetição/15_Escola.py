"""15) - A escola “APRENDER” faz o pagamento de seus professores por hora/aula.
Faça um algoritmo que calcule e exiba o salário do professor.
Sabe-se que o valor da hora/aula segue a tabela abaixo:
    Professor Nível 1 R$12,00 por hora/aula
    Professor Nível 2 R$17,00 por hora/aula
    Professor Nível 3 R$25,00 por hora/aula
    A escola "APRENDER” possui 50 professores."""

professores = 50

print("-------ESCOLA APRENDER-------")
for i in range(1, professores + 1):

    nome = input("Informe o nome do professor: ")
    print("=" * 90)
    print(f"Professor {i} Nome: {nome}")
    print("=" * 90)
    nivel = int(input("Informe o nível do professor (1 a 3): "))

    match nivel:
        case 1:
            aula = 12.00
            dia = aula * 6
            salario_mes = dia * 30
            print("=" * 90)
            print(f"Professor {i} Nome: {nome} Salario tem o salario mensal de: {salario_mes}")
            print("=" * 90)
        case 2:
            aula = 17.00
            dia = aula * 6
            salario_mes = dia * 30
            print("=" * 90)
            print(f"Professor {i} Nome: {nome} Salario tem o salario mensal de: {salario_mes}")
            print("=" * 90)
        case 3:
            aula = 25.00
            dia = aula * 6
            salario_mes = dia * 30
            print("=" * 90)
            print(f"Professor {i} Nome: {nome} Salario tem o salario mensal de: {salario_mes}")
            print("=" * 90)
        case _:
            print("Nível inválido, tente novamente.")
