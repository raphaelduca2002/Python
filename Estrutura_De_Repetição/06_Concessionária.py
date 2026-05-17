"""06) - A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto.
Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros.
O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%.
O sistema deverá perguntar se o usuário deseja continuar calculando desconto até que a resposta seja:
“(N) Não”. Informar total de carros com ano até 2000, total de carros acima do ano 2000 e o total geral."""

# Inicialização dos contadores e totais
total_carros_ate_2000 = 0
total_carros_acima_2000 = 0
total_geral_carros = 0
continuar = 'S'

print("--- SISTEMA DE DESCONTOS CARANGO VELHO ---")

while continuar.upper() == 'S':
    # Entrada de dados
    try:
        ano = int(input("Digite o ano do veículo: "))
        valor_veiculo = float(input("Digite o valor do veículo: R$ "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue

    # Cálculo do desconto baseada no ano
    if ano <= 2000:
        desconto = valor_veiculo * 0.12  # 12%
        total_carros_ate_2000 += 1
    else:
        desconto = valor_veiculo * 0.07  # 7%
        total_carros_acima_2000 += 1

    valor_final = valor_veiculo - desconto
    total_geral_carros += 1

    # Exibição dos resultados do carro atual
    print("-" * 30)
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
    print("-" * 30)

    # Pergunta se deseja continuar
    continuar = input("Deseja continuar calculando? (S)im / (N)ão: ")
    while continuar.upper() not in ['S', 'N']:
        continuar = input("Opção inválida. Digite S para Sim ou N para Não: ")

# Exibição dos totais finais
print("\n--- RESUMO FINAL ---")
print(f"Total de carros com ano até 2000: {total_carros_ate_2000}")
print(f"Total de carros com ano acima de 2000: {total_carros_acima_2000}")
print(f"Total geral de carros: {total_geral_carros}")
input("Pressione qualquer tecla para encerrar o programa.")