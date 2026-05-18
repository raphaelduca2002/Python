# Estrutura de Decisão


valor = int(input("Informe um valor: "))

# Verificar se a variável é maior que 10

# Decisão Simples

if valor == 10:
    print(f"O Valor informado {valor} é igual a 10.")
if valor > 10:
    print(f"O Valor informado {valor} é maior que 10.")

# Decisão Composta

else:
    if valor < 10:
        print(f"O Valor informado {valor} é menor que 10")
