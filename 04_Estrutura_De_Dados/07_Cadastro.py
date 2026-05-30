"""7) - Desenvolva um programa em python que receba valores numéricos informado pelo usuário e cadastre-os em uma lista,
caso a lista já contenha o valor informado, exibir a mensagem "Valor já cadastrado".
No final exiba todos os valores cadastrados."""

valores_numericos = []
continuar = "S"

while continuar.upper() == "S":
    try:
        numero = int(input("Informe um número: "))
    except ValueError:
        print("Valor incorreto!")
        continue

    if numero not in valores_numericos:
        valores_numericos.append(numero)
    else:
        print("O Número já foi cadastrado, tente novamente.")

    continuar = input("Deseja continuar? [S/N]: ")

    while continuar.upper() not in ['S', 'N']:
        continuar = input("Opção inválida. Digite S para continuar ou N para encerrar: ")

print("-" * 30)
print("Números Cadastrados:")
print(valores_numericos)
print("-" * 30)
input("Pressione qualquer tecla para sair")
