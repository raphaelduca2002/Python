"""3. Desenvolva um algoritmo que receba as 4 notas bimestrais e ao final exiba a média aritmética."""

#  Entrada de Dados e variáveis


nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

#  Processamento de Dados

media = (nota1 + nota2 + nota3 + nota4) / 4

#  Saída de Dados

print("A Média do aluno é: ", media)

#  Formatado

print(f"A Média do aluno é: {media}")

if media >= 6:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

#  FIM
