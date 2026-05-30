"""15) - [DESAFIO] Desenvolva um procurado em python que leia valores inteiros para um vetor de 20 posições e
mostre-o. Em seguida, troque o primeiro elemento pelo último, o segundo com o penúltimo, o terceiro com o
antepenúltimo e, assim, sucessivamente. Mostre o novo vetor após todas as trocas."""

vetor = []


# for i in range(1, 21, 1):
#     valor = int(input(f"{i}/20 Informe um valor: "))
#     vetor.append(valor)

for i in range(1, 21):
    vetor.append(i)

print(vetor)

vetor_comprimento = len(vetor)

for i in range(vetor_comprimento // 2):
    aux = vetor[i]
    vetor[i] = vetor[vetor_comprimento - 1 - i]
    vetor[vetor_comprimento - 1 - i] = aux
print("Novas posições no vetor:")
print(vetor)
input("Pressione qualquer tecla para sair")