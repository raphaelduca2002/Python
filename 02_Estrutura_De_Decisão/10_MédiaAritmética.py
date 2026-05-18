"""10.	Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre.
Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5)
e Recuperação (media entre 5,1 a 6,9).
"""

aluno = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"o Aluno: {aluno} está Aprovado, média: {media}")
elif media <= 5:
    print(f"o Aluno: {aluno} está Reprovado, média: {media}")
elif 5.1 <= media <= 6.9:
    print(f"o Aluno {aluno} está de recuperação, media: {media}")