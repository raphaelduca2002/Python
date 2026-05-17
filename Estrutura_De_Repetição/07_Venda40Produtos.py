"""07) - Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos.
Mostre como resultado se houve lucro, prejuízo ou empate para cada produto.
Informe média de preço de custo e do preço de venda."""

total_custo = 0
total_venda = 0
produtos = 40

print(f"---SISTEMA DE ANÁLISE DE {produtos} PRODUTOS---")

for i in range(1, produtos + 1):
    print(f"\nProduto {i}")
    custo = float(input("Insira o preço de custo: R$ "))
    venda = float(input("Insira o preço de venda: R$ "))
    total_custo = total_custo + custo
    total_venda = total_venda + venda

    if venda > custo:
        resultado = "Lucro"
    elif venda < custo:
        resultado = "Prejuízo"
    else:
        resultado = "Empate"

    print(f"{resultado}")

media_custo = total_custo / produtos
media_venda = total_venda / produtos

print("\n" + "=" * 30)
print(f"Média de preço de custo dos produtos informados: {media_custo:.2f} R$")
print(f"Média de valor de venda dos produtos informados: {media_venda:.2f} R$")
if media_custo > media_venda:
    print("Prejuízo")
elif media_custo < media_venda:
    print("Lucro")
print("=" * 30)
input("Pressione qualquer tecla para sair...")
