"""13) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
      Ao final exibir quantos valores estão no intervalo, quantos são pares e quantos são ímpares."""

valor_inicial = int(input("Insira o valor inicial: "))
valor_final = int(input("Insira o valor final: "))


inicio = min(valor_inicial, valor_final)
final = max(valor_inicial, valor_final)

total_de_valores = 0
pares = 0
impares = 0

for numero in range(inicio, final + 1):
    total_de_valores = numero
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é Par")
    else:
        impares += 1
        print(f"{numero} é Impar")

print("-" * 40)
print(f"Intervalo analisado: {inicio} até {final}")
print(f"Total de valores no intervalo: {total_de_valores}")
print(f"Quantidade de números PARES: {pares}")
print(f"Quantidade de números ÍMPARES: {impares}")
print("-" * 40)
