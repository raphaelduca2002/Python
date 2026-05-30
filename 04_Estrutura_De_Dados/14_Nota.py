"""14) Desenvolva um programa em python que leia o nome e uma nota para um aluno,
crie duas listas para armazenar estes valores, o usuário deverá informar um nome de aluno para a pesquisar,
se o aluno existir na lista com os nomes do aluno, exibir o nome e a nota do aluno, caso contrário informar a
mensagem "Aluno não cadastrado."
"""

alunos = []
notas = []
continuar = "S"

print("-" * 5 + "Cadastro de alunos" + "-" * 5)

while continuar == "S":
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos.append(nome.upper())
    notas.append(nota)

    opcao = input("Deseja continuar? [S/N]: ")
    while opcao.upper() != "S" and opcao.upper() != "N":
        opcao = input("Valores incorretos, informe S para continuar ou N para encerrar: ")
    if opcao.upper() == "N":
        break
print("-" * 30)
print("Alunos cadastrados")
print(alunos)
print("-" * 30)

while True:
    buscar = input("Informe o nome do aluno para pesquisar na lista: ").upper()
    if buscar in alunos:
        indice = alunos.index(buscar)
        print("-" * 30)
        print(f"Nome: {alunos[indice]} | Nota: {notas[indice]}")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Aluno não cadastrado")
        print("-" * 45)
        break
input("Pressione qualquer tecla para encerrar...")
print("-" * 45)
