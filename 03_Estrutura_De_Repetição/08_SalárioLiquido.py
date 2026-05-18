"""08) - Faça um algoritmo que receba o nome a idade e o sexo de dez funcionário. Para cada funcionário mostre o nome e o salário líquido:
      SEXO	IDADE	SALÁRIO LÍQUIDO
      M		>= 30	R$ 100,00
      M		< 30	R$ 50,00
      F		>= 30	R$ 200,00
      F		< 30	R$ 80,00"""

funcionarios_cadastrados = []

print("=" * 85)
print("Algoritmo para mostrar o salário líquido de cada funcionário baseado na idade e sexo.")
print("=" * 85)

for funcionarios in range(1, 11, 1):
    print(f"Funcionario(a) {funcionarios}")
    nome = input(f"Informe o nome do funcionário: ")
    idade = int(input(f"Informe a idade do funcionario {nome}: "))
    sexo = input(f"Informe o sexo do funcionario (M / F): ")
    # if sexo.upper() != "M" and sexo.upper() != "F":
    #     print("Dados inválidos")
    #     sexo = input(f"Informe o sexo do funcionario (M / F): ")

    if idade >= 30 and sexo.upper() == "M":
        print("=" * 30)
        print(f"Funcionário: {nome}")
        print("Salário líquido: R$ 100,00")
        print("=" * 30)
        funcionario_nome = nome
        funcionarios_cadastrados.append(f"Nome: {funcionario_nome} idade: {idade} Sexo: {sexo} ID: {funcionarios}")

    elif idade < 30 and sexo.upper() == "M":
        print("=" * 30)
        print(f"Funcionário: {nome}")
        print("Salário liquido: R$ 50,00")
        print("=" * 30)
        funcionario_nome = nome
        funcionarios_cadastrados.append(f"Nome: {funcionario_nome} Idade: {idade} Sexo: {sexo} ID: {funcionarios}")

    elif idade >= 30 and sexo.upper() == "F":
        print("=" * 30)
        print(f"Funcionária: {nome}")
        print("Salário líquido: R$ 200,00")
        print("=" * 30)
        funcionario_nome = nome
        funcionarios_cadastrados.append(f"Nome: {funcionario_nome} Idade: {idade} Sexo: {sexo} ID: {funcionarios}")

    elif idade < 30 and sexo.upper() == "F":
        print("=" * 30)
        print(f"Funcionária: {nome}")
        print("Salário líquido: R$ 80,00")
        print("=" * 30)
        funcionario_nome = nome
        funcionarios_cadastrados.append(f"Nome: {funcionario_nome} Idade: {idade} sexo: {sexo}")

    continuar = input("Pressione qualquer tecla para continuar ou N para encerrar: ")
    if continuar == "N" or continuar =="n":
        print("=" * 30)
        print("Funcionários: ")
        print("=" * 30)
        for funcionarios_cadastrados in funcionarios_cadastrados:
            print(funcionarios_cadastrados)
        break
    print("=" * 30)
    print("Funcionários: ")
    print("=" * 30)
    print(*sorted(funcionarios_cadastrados), sep='\n')
    print("=" * 30)

print("=" * 30)
input("Pressione qualquer tecla do teclado para encerrar o programa...")




