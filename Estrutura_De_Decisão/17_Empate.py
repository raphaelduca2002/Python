"""17.	Escreva um algoritmo que leia o nome de 2 times e o número de gols marcados na partida (para cada time).
 Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE."""

time1 = input("Informe o nome do time 1: ")
time2 = input("Informe o nome do time 2: ")

gols_time1 = int(input(f"Informe a quantidade de gols do {time1}: "))
gols_time2 = int(input(f"Informe o quantidade de gols do {time2}: "))

if gols_time1 > gols_time2:
    print(f"{time1} venceu!")
    print(f"{time2} perdeu!")

elif gols_time1 < gols_time2:
    print(f"{time1} perdeu!")
    print(f"{time2} venceu!")

elif gols_time1 == gols_time2:
    print(f"{time1} e {time2} empataram!")

