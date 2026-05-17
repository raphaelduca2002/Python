"""02) - Escrever um algoritmo que leia os dados de “N” pessoas (nome, idade e saúde) e informe se está apta ou não
para cumprir o serviço militar obrigatório. Informe os totais."""

# Descobrir se a pessoa está apta para o serviço militar.
# Idade tem que ser maior ou igual a 18 anos.
# Se a saúde estiver OK.

continuar = True
qtd_pessoa_apta = 0
qtd_pessoa_inapta = 0
# Lista vazia de candidatos aprovados
candidatos_aptos = []
candidaturas = 0

print("--------------------CANDIDATOS DO EXÉRCITO---------------------")
print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
while continuar:
    print("===============================================================")
    try:
        candidato_nome = input("Informe o nome do candidato: ")
        candidato_idade = int(input("Informe a idade do candidato: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue
    saude = input("Informe A para saúde OK ou I para problema de saúde: ")

    if candidato_idade >= 18 and saude.upper() == "A":
        print("===============================================================")
        print(f"o Candidato {candidato_nome} está apto para o serviço militar.")
        print("===============================================================")
        qtd_pessoa_apta = qtd_pessoa_apta + 1
        # Adicionando os dados do candidato aprovado na lista vazia
        candidato_aprovado = candidato_nome
        candidatos_aptos.append(
            f"Nome: {candidato_aprovado}, idade: {candidato_idade} anos, Condição de saúde: {saude.upper()} (saudável).")
    else:
        print("===============================================================")
        print(f"o Candidato {candidato_nome} não está apto para o serviço militar.")
        print(f"o Candidato {candidato_nome} é menor de Idade ou possuí problema de saúde.")
        qtd_pessoa_inapta = qtd_pessoa_inapta + 1
        print("===============================================================")

    candidaturas = candidaturas + 1

    print(f"Fim da candidatura")

    opcao = input("Digite N para sair ou pressione qualquer tecla para gerar outra candidatura: ")

    if opcao.upper() == "N":
        # Resultados
        print("===============================================================")
        print(f"Quantidade de candidaturas: {candidaturas}")
        print(f"Aptos: {qtd_pessoa_apta}")
        print(f"Inaptos: {qtd_pessoa_inapta}")
        print("Candidatos aprovados:")
        print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
        for candidatos in candidatos_aptos:
            print(candidatos)
        print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
        input("Pressione qualquer tecla para sair.")

        continuar = False
