"""5) - [Desafio]
Escreva um programa que corrija a prova dos alunos de uma classe.
A prova consta de 30 questões, cada uma com cinco alternativas (a, b, c, d, e).
O programa receberá os seguintes dados: o cartão gabarito; o número de alunos da turma;
o cartão de respostas de cada aluno, contendo o seu número e suas respostas.
A partir daí o programa deverá comparar as respostas de cada aluno com a resposta do gabarito e, no final,
exibir os pontos que cada aluno obteve."""


def corrigir_prova():
    print("Informe o Gabarito Oficial de 30 questões (abcde...)")
    gabarito = []

    for i in range(1, 31, 1):
        while True:
            respostas = input(f"Informe a resposta correta da questão {i} (a, b, c, d, e): ")
            if respostas in ["a", "b", "c", "d", "e"]:
                gabarito.append(respostas)
                break
            print("Opção inválida, Digite apenas a, b, c, d ou e.")

    qtd_alunos = int(input("Informe quantos alunos realizaram a prova: "))

    print("---Processamento das provas---")

    resultados = []

    for aluno in range(1, qtd_alunos + 1):

        print(f"Aluno {aluno}: ")
        numero_aluno = int(input("Informe o RA do aluno: "))

        pontos = 0
        respostas_aluno = []

        for i in range(30):
            while True:
                resp = input(f"Questão {i + 1} (a, b, c, d, e): ").strip().lower()
                if resp in ['a', 'b', 'c', 'd', 'e']:
                    respostas_aluno.append(resp)
                    break
                print("Opção inválida! Digite apenas a, b, c, d ou e.")

        for i in range(30):
            if respostas_aluno[i] == gabarito[i]:
                pontos += 1

        resultados.append({"id": numero_aluno, "pontos": pontos})

    print("=" * 30)
    print("RESULTADO FINAL DA TURMA")
    print("=" * 30)
    for i in resultados:
        print(f"Aluno Nº {i['id']}: {i['pontos']} pontos")

corrigir_prova()