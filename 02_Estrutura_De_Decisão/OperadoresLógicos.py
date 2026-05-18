A = 3
B = 4
C = 8

resposta_a = A > 3 and C == 8
print(f"a) A > 3 e C = 8 é {resposta_a}")

resposta_b = A != 2 or B <= 5
print(f"b) A <> 2 ou B <= 5 é {resposta_b}")

resposta_c = A == 3 or B >= 2 and C == 8
print(f"c) A = 3 ou B >= 2 e C = 8 é {resposta_c}")

resposta_d = A == 3 and not B <= 4 and C == 8
print(f"d) A = 3 e não B <= 4 e C = 8 é {resposta_d}")

resposta_e = A != 8 or B == 4 and C > 2
print(f"e) A <> 8 ou B = 4 e C > 2 {resposta_e}")

resposta_f = B > A and C != A
print(f"f) B > A e C <> A é {resposta_f}")

resposta_g = A > B or B < 5
print(f"g) A > B ou B < 5 é {resposta_g}")

resposta_h = A != B and B == C
print(f"h) A <> B e B = C é {resposta_h}")

resposta_i = C > 2 or A < B
print(f"i) C > 2 ou A < B é {resposta_i}")

resposta_j = A > B or B > A and C != B
print(f"j) A > B ou B > A e C <> B é {resposta_j}")
