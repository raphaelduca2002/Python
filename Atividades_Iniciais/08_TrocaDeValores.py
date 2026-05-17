"""8. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a
possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados."""

#  Entrada de Dados

A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))

#  Processamento de Dados

C = A
A = B
B = C

#  Saída de Dados

print("Valores Trocados!")
print(f"O valor de A é de: {A}")
print(f"O valor de B é de: {B}")
