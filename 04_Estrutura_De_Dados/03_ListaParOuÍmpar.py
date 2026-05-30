"""3) - Desenvolva um programa em python que receba 15 valores informados pelo usuário armazene-os em vetor chamado
num, e imprima uma listagem numerada contendo a seguinte mensagem "Par" ou "Ímpar" de acordo com os valores
cadastrados no vetor."""

num = []
# if numero % 2 == 0:

for x in range(1, 16, 1):
    print(f"({x}/15)")
    num.append(int(input(f"Informe o {x}º valor: ")))

contador = 1

print("-" * 30)

for numeros in num:
    if numeros % 2 == 0:
        print(f"{contador} - {numeros} Par")
        contador += 1
    else:
        print(f"{contador} - {numeros} Ímpar")
        contador += 1

print("-" * 30)
print(num)

