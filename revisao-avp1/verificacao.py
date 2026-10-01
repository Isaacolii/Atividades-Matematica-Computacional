"""
Lista de Revisão - AVP1 (Conjuntos e Funções)
Conferência em Python das respostas: conjuntos com set, frações exatas com Fraction e o resto com math.
"""
import math
from fractions import Fraction as Fr


def mostra(valor):
    # Conjuntos em ordem crescente, frações como 3/4 e decimais com 6 algarismos significativos
    if isinstance(valor, (set, frozenset)):
        return "{" + ", ".join(str(v) for v in sorted(valor)) + "}"
    if isinstance(valor, (list, tuple)):
        itens = ", ".join(mostra(v) for v in valor)
        return f"[{itens}]" if isinstance(valor, list) else f"({itens})"
    if isinstance(valor, float):
        return f"{valor:.6g}"
    return str(valor)


def confere(questao, obtido, esperado):
    if isinstance(esperado, float):
        ok = math.isclose(obtido, esperado, rel_tol=1e-9, abs_tol=1e-9)
    else:
        ok = obtido == esperado
    assert ok, f"Questão {questao}: obtido {obtido}, esperado {esperado}"
    print(f"Questão {questao:>2}: {mostra(obtido)}  OK")


# ---------- Conjuntos ----------

# 1 - união, interseção e diferença
A, B = {10, 15, 20, 25, 30}, {20, 30, 40, 50}
confere(1, A | B, {10, 15, 20, 25, 30, 40, 50})
confere(1, A & B, {20, 30})
confere(1, A - B, {10, 15, 25})
confere(1, len(A | B), len(A) + len(B) - len(A & B))

# 2 - complementar de A em U
U = set(range(1, 11))
A = {1, 2, 4, 5, 7, 9}
confere(2, U - A, {3, 6, 8, 10})

# 3 - B \ A = B ∩ complementar de A, testado em todos os pares de subconjuntos de um universo pequeno
U = {1, 2, 3, 4, 5}
subconjuntos = [{x for x in U if (mascara >> (x - 1)) & 1} for mascara in range(2 ** len(U))]
confere(3, all(B - A == B & (U - A) for A in subconjuntos for B in subconjuntos), True)

# 4 - oficinas de programação (P) e análise de dados (D)
P, D = {1, 2, 3, 5, 7, 8}, {2, 3, 4, 7, 9}
confere(4, P | D, {1, 2, 3, 4, 5, 7, 8, 9})
confere(4, P & D, {2, 3, 7})
confere(4, P ^ D, {1, 4, 5, 8, 9})
confere(4, (P - D, D - P), ({1, 5, 8}, {4, 9}))

# ---------- Função afim ----------

# 5 - raiz de f(x) = 3x - 12
confere(5, Fr(12, 3), 4)

# 6 - C(g) = 100 + 0,02g
C = lambda g: 100 + Fr(2, 100) * g
confere(6, C(5000), 200)
confere(6, (300 - 100) / Fr(2, 100), 10000)

# 7 - T(t) = -2t + 28
T = lambda t: -2 * t + 28
confere(7, (T(0), T(1) - T(0), Fr(28, 2), T(14)), (28, -2, 14, 0))

# 8 - A(x) = 50 + 4x e B(x) = 20 + 5x
custo_A = lambda x: 50 + 4 * x
custo_B = lambda x: 20 + 5 * x
confere(8, (custo_A(30), custo_B(30)), (170, 170))
confere(8, (custo_A(10), custo_B(10)), (90, 70))    # B mais barato
confere(8, (custo_A(40), custo_B(40)), (210, 220))  # A mais barato

# 9 - reta pelos pontos (2, 15) e (8, 45)
v = Fr(45 - 15, 8 - 2)
s0 = 15 - v * 2
s = lambda t: v * t + s0
confere(9, (v, s0, s(8), s(12)), (5, 5, 45, 65))

# 10 - variação vertical para Δx = 300 com inclinação de 30°
m = math.tan(math.radians(30))
confere(10, m, math.sqrt(3) / 3)
confere(10, m * 300, 100 * math.sqrt(3))

# ---------- Função quadrática ----------


def vertice(a, b, c):
    xv = Fr(-b, 2 * a)
    return xv, a * xv ** 2 + b * xv + c


# 11 - L(x) = -x² + 10x - 21: raízes 3 e 7, positivo entre elas
L = lambda x: -x ** 2 + 10 * x - 21
confere(11, (L(3), L(7)), (0, 0))
confere(11, (L(2) < 0, L(5) > 0, L(8) < 0), (True, True, True))
confere(11, vertice(-1, 10, -21), (5, 4))

# 12 - h(t) = -5t² + 20t + 2: máximo em t = 2 com h = 22
confere(12, vertice(-5, 20, 2), (2, 22))

# 13 - R(x) = -2x² + 16x + 10: vértice (4, 42)
confere(13, vertice(-2, 16, 10), (4, 42))

# ---------- Função racional ----------

# 14 - T(x) = 10/(x - 2) cresce sem limite perto de x = 2
T = lambda x: Fr(10) / (x - 2)
confere(14, [T(Fr(19, 10)), T(Fr(199, 100)), T(Fr(201, 100)), T(Fr(21, 10))], [-100, -1000, 1000, 100])

# 15 - R(x) = (x + 4)/(x - 3) perto de x = 3
R = lambda x: (x + 4) / (x - 3)
confere(15, [R(Fr(29, 10)), R(Fr(299, 100)), R(Fr(301, 100)), R(Fr(31, 10))], [-69, -699, 701, 71])

# ---------- Exponencial e logaritmo ----------

# 16 - M(t) = 4000 · 1,10^t
M = lambda t: 4000 * Fr(110, 100) ** t
confere(16, M(3), 5324)
confere(16, [M(1) - M(0), M(2) - M(1), M(3) - M(2)], [400, 440, 484])

# 17 - 5000 · 1,12^t = 15000  ->  t = log 3 / log 1,12
t = 0.4771 / 0.0492
confere(17, round(t, 2), 9.70)
confere(17, round(math.log(3) / math.log(1.12), 2), 9.69)  # com logaritmos sem arredondar
confere(17, (round(5000 * 1.12 ** 9, 2), round(5000 * 1.12 ** 10, 2)), (13865.39, 15529.24))

# 18 - log2(x) = 6
confere(18, (2 ** 6, math.log2(64)), (64, 6.0))

# ---------- Trigonometria ----------

# 19 - h(t) = 5 + 4 sen(πt/2): mínima 1, máxima 9, período 4
h = lambda t: 5 + 4 * math.sin(math.pi * t / 2)
amostras = [i / 1000 for i in range(8000)]
confere(19, (round(min(map(h, amostras)), 6), round(max(map(h, amostras)), 6)), (1.0, 9.0))
confere(19, (h(1), h(3)), (9.0, 1.0))
confere(19, all(math.isclose(h(t + 4), h(t), abs_tol=1e-9) for t in amostras), True)

# 20 - coeficiente angular e variação vertical para alguns ângulos
for angulo, delta_y in [(30, 100 * math.sqrt(3)), (45, 300.0), (60, 300 * math.sqrt(3))]:
    confere(20, 300 * math.tan(math.radians(angulo)), delta_y)
