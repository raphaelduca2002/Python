"""09) - Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado.
Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir apólices de seguro.
Quanto às classes de ocupações, foram definidos três grupos de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco.
Dados nome, idade e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro.
Imprimir o nome a idade e a categoria do pretendente e caso a idade não esteja na faixa necessária, imprimir uma mensagem.
	  GRUPO DE RISCO
	  IDADE			BAIXO		MEDIO		ALTO
	  17 A 20		1			2			3
	  21 A 24		2			3			4
	  25 A 34		3			4			5
	  35 A 64		4			5			6
	  65 A 70		7			8			9"""

continuar = True

print("----------SEGURADORA LEGAL----------")
while continuar:
    nome = input("Informe o nome do(a) segurado(a): ")
    idade = int(input("Informe a idade: "))
    if 17 <= idade <= 20:
        categoria = int(input("Informe a categoria de 1 a 3: "))
        match categoria:
            case 1:
                categoria = "Categoria de risco 1 (Baixa)"
            case 2:
                categoria = "Categoria de risco 2 (Média)"
            case 3:
                categoria = "Categoria de risco 3 (Alta)"
            case _:
                categoria = "Categoria inválida"

        if categoria == "Categoria de risco 1 (Baixa)":
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} não poderá receber do seguro.")
            print("=" * 120)
        elif categoria == "Categoria inválida":
            print("=" * 120)
            print("a Categoria informada é inválida, tente novamente.")
            print("=" * 120)
        else:
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} tem o direito de receber o seguro.")
            print("=" * 120)

    elif 21 <= idade <= 24:
        categoria = int(input("Informe a categoria de 2 a 4: "))

        match categoria:

            case 2:
                categoria = "Categoria de risco 2 (Baixa)"
            case 3:
                categoria = "Categoria de risco 3 (Média)"
            case 4:
                categoria = "Categoria de risco 4 (Alta)"
            case _:
                print("Categoria inválida")
                categoria = "Categoria inválida"

        if categoria == "Categoria de risco 2 (Baixa)":
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} não poderá receber do seguro.")
            print("=" * 120)
        elif categoria == "Categoria inválida":
            print("=" * 120)
            print("a Categoria informada é inválida, tente novamente.")
            print("=" * 120)
        else:
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} tem o direito de receber o seguro.")
            print("=" * 120)

    elif 25 <= idade <= 34:
        categoria = int(input("Informe a categoria de 3 a 5: "))

        match categoria:
            case 3:
                categoria = "Categoria de risco 3 (Baixa)"
            case 4:
                categoria = "Categoria de risco 4 (Média)"
            case 5:
                categoria = "Categoria de risco 5 (Alta)"
            case _:
                print("Categoria inválida")
                categoria = "Categoria inválida"

        if categoria == "Categoria de risco 3 (Baixa)":
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} não poderá receber do seguro.")
            print("=" * 120)
        elif categoria == "Categoria inválida":
            print("=" * 120)
            print("a Categoria informada é inválida, tente novamente.")
            print("=" * 120)
        else:
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} tem o direito de receber o seguro.")
            print("=" * 120)

    elif 35 <= idade <= 64:
        categoria = int(input("Informe a categoria de 4 a 6: "))

        match categoria:
            case 4:
                categoria = "Categoria de risco 4 (Baixa)"
            case 5:
                categoria = "Categoria de risco 5 (Média)"
            case 6:
                categoria = "Categoria de risco 6 (Alta)"
            case _:
                print("Categoria inválida")
                categoria = "Categoria inválida"

        if categoria == "Categoria de risco 4 (Baixa)":
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} não poderá receber do seguro.")
            print("=" * 120)
        elif categoria == "Categoria inválida":
            print("=" * 120)
            print("a Categoria informada é inválida, tente novamente.")
            print("=" * 120)
        else:
            print("=" * 120)
            print(f"O(A) Segurado(a): {nome} de {idade} anos da {categoria} tem o direito de receber o seguro.")
            print("=" * 120)

    elif 65 <= idade <= 70:
        categoria = int(input("Informe a categoria de 7 a 9: "))

        match categoria:
            case 7:
                categoria = "Categoria de risco 7 (Baixa)"
            case 8:
                categoria = "Categoria de risco 8 (Média)"
            case 9:
                categoria = "Categoria de risco 9 (Alta)"
            case _:
                print("Categoria inválida")
                categoria = "Categoria inválida"

        if categoria == "Categoria de risco 4 (Baixa)":
            print("=" * 120)
            print(f"O Segurado: {nome} de {idade} anos da {categoria} não poderá receber do seguro.")
            print("=" * 120)
        elif categoria == "Categoria inválida":
            print("=" * 120)
            print("a Categoria informada é inválida, tente novamente.")
            print("=" * 120)
        else:
            print("=" * 120)
            print(f"O Segurado: {nome} de {idade} anos da {categoria} tem o direito de receber o seguro.")
            print("=" * 120)

    else:
        print("Idade inválida tente novamente.")

    opcao = input("Pressione qualquer tecla para tentar novamente ou pressione N para encerrar o programa: ")
    if opcao.upper() == "N":
        print("-" * 32)
        input("Programa finalizado com sucesso! ")
        continuar = False
