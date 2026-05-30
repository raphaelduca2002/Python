"""9) - Desenvolva um programa em python que leia 10 valores numéricos informados pelo usuário
e armazene-os em um vetor A, leia mais 10 valores numéricos informado pelo usuário
armazene-os em outro vetor B, Gere um vetor C, que receberá a soma dos elementos do vetor A e B
na sua respectiva posição. Ao final exibir os três vetores A, B e C.
"""

vetor_a = []
vetor_b = []
vetor_c = []

print("Vetor A: ")
for i in range(1, 11, 1):
    valor = int(input(f"{i}/10: Informe um valor para o vetor A: "))
    vetor_a.append(valor)

print("Vetor B: ")
for i in range(1, 11, 1):
    valor = int(input(f"{i}/10: Informe um valor para o vetor B: "))
    vetor_b.append(valor)

for i in range(10):
    soma_vetores = vetor_a[i] + vetor_b[i]
    vetor_c.append(soma_vetores)

print("-" * 20 + "Vetores" + "-" * 20)
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Vetor C: {vetor_c}")

