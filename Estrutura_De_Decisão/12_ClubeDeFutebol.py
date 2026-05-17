"""12.	Um determinado clube de futebol pretende classificar seus atletas em categorias e para isto ele contratou
um programador para criar um programa que executasse esta tarefa. Para isso o clube criou uma tabela que continha
a faixa etária do atleta e sua categoria. A tabela está demonstrada abaixo:
IDADE 		CATEGORIA
De 05 a 10	Infantil
De 11 a 15	Juvenil
De 16 a 20 	Junior
De 21 a 25 	Profissional
Construa um programa que solicite o nome e a idade de um atleta e imprima a sua categoria."""

atleta = input("Informe o nome do atleta: ")
idade = int(input("Informe a idade do atleta: "))

if 5 <= idade <= 10:
    print(f"O atleta {atleta} tem {idade} anos e faz parte da categoria Infantil.")
elif 11 <= idade <= 15:
    print(f"O atleta {atleta} tem {idade} anos e faz parte da categoria Juvenil.")
elif 16 <= idade <= 20:
    print(f"O atleta {atleta} tem {idade} anos e faz parte da categoria Junior.")
elif 21 <= idade <= 25:
    print(f"O atleta {atleta} tem {idade} anos e faz parte da categoria Profissional.")
else:
    print("Idade Inválida!")

