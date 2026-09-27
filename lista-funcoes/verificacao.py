"""
Lista de Revisão Geral - Funções
Conferência em Python das respostas: frações exatas com Fraction e contas com ponto flutuante com math.
"""
import math
from fractions import Fraction as Fr


def mostra(valor):
    # Frações como -3/4 e números decimais com 6 algarismos significativos
    if isinstance(valor, (list, tuple)):
        itens = ", ".join(mostra(v) for v in valor)
        return f"[{itens}]" if isinstance(valor, list) else f"({itens})"
    if isinstance(valor, float):
        return f"{valor:.6g}"
    return str(valor)


def confere(questao, obtido, esperado):
    if isinstance(esperado, float):
        ok = math.isclose(obtido, esperado, rel_tol=1e-9, abs_tol=1e-12)
    else:
        ok = obtido == esperado
    assert ok, f"Questão {questao}: obtido {obtido}, esperado {esperado}"
    print(f"Questão {questao:>2}: {mostra(obtido)}  OK")


# ---------- Função linear ----------

# 1 - reta 3x + 4y - 3 = 0: m = -3/4, corta o eixo x em (1, 0) e o eixo y em (0, 3/4)
m = Fr(-3, 4)
confere(1, (m, Fr(3, 3), Fr(3, 4)), (Fr(-3, 4), 1, Fr(3, 4)))

# 2 - reta por P(1, 2) e Q(-3, 7): y = -5/4 x + 13/4, ou 5x + 4y - 13 = 0
m = Fr(7 - 2, -3 - 1)
b = 2 - m * 1
confere(2, (m, b, 5 * (-3) + 4 * 7 - 13), (Fr(-5, 4), Fr(13, 4), 0))

# 3 - inclinação de 60° por P(1, 2): y = √3 x + 2 - √3
m = math.tan(math.radians(60))
confere(3, m, math.sqrt(3))
confere(3, math.sqrt(3) * 1 + 2 - math.sqrt(3), 2.0)  # a reta passa por P

# 4 - perpendicular a f(x) = 3x - 8 pela origem: y = -x/3
m2 = Fr(-1, 3)
confere(4, 3 * m2, -1)

# ---------- Função quadrática ----------


def bhaskara(a, b, c):
    delta = b * b - 4 * a * c
    raiz = math.isqrt(delta)
    return sorted({Fr(-b - raiz, 2 * a), Fr(-b + raiz, 2 * a)}), (Fr(-b, 2 * a), Fr(-delta, 4 * a))


# 5 - f(x) = x² - 9x + 18: raízes 3 e 6, vértice (9/2, -9/4)
confere(5, bhaskara(1, -9, 18), ([3, 6], (Fr(9, 2), Fr(-9, 4))))

# 6 - f(x) = -3x² + 18x - 27: raiz dupla 3, vértice (3, 0)
confere(6, bhaskara(-3, 18, -27), ([3], (3, 0)))

# 7 - parábola por (-1, 16), (0, 11) e (1, 16): f(x) = 5x² + 11
f = lambda x: 5 * x ** 2 + 11
confere(7, [f(-1), f(0), f(1)], [16, 11, 16])

# 8 - vértice (-1, 8) e passa por (-5, 56): f(x) = 3x² + 6x + 11
f = lambda x: 3 * x ** 2 + 6 * x + 11
confere(8, (f(-1), f(-5), Fr(-6, 2 * 3)), (8, 56, -1))

# ---------- Função exponencial ----------

# 9 - 5³ · 5² = 5⁵
confere(9, 5 ** 3 * 5 ** 2, 5 ** 5)

# 10 - 100^x = 0,001 com x = -3/2
confere(10, 100 ** -1.5, 0.001)

# 11 - 8^(2x - 1) = 0,25 com x = 1/6
confere(11, 8 ** (2 * (1 / 6) - 1), 0.25)

# 12 - 1 + 5 + 5² + ... + 5¹⁰ pela fórmula da soma da PG
confere(12, sum(5 ** k for k in range(11)), (5 ** 11 - 1) // (5 - 1))

# 13 - f(x) = 2^(1 - x): f(0) = 2 e é decrescente
f = lambda x: 2 ** (1 - x)
confere(13, (f(0), f(0) > f(1) > f(2)), (2, True))

# ---------- Função logarítmica ----------

# 14 - log na base 25 de 0,008 = -3/2
confere(14, math.log(0.008, 25), -1.5)

# 15 - log 15 = 1 - a + b, com a = log 2 e b = log 3
a, b = math.log10(2), math.log10(3)
confere(15, 1 - a + b, math.log10(15))

# 16 - 2^(3x - 2) = 3^(2x + 1) com x = log 12 / log(8/9)
x = math.log(12) / math.log(8 / 9)
confere(16, round(x, 2), -21.1)
confere(16, 2 ** (3 * x - 2), 3 ** (2 * x + 1))

# 17 - log2(x - 1): domínio x > 1 e raiz x = 2
confere(17, math.log2(2 - 1), 0.0)

# 18 - log na base (x - 1) de (x³ - x² + x - 3) = 3 com x = (1 + √5)/2
x = (1 + math.sqrt(5)) / 2
base, logaritmando = x - 1, x ** 3 - x ** 2 + x - 3
confere(18, (base > 0, base != 1, logaritmando > 0), (True, True, True))
confere(18, math.log(logaritmando, base), 3.0)
confere(18, (1 - math.sqrt(5)) / 2 - 1 < 0, True)  # a outra raiz deixa a base negativa

# ---------- Funções trigonométricas ----------

# 19 - 300° = 5π/3 rad
confere(19, math.radians(300), 5 * math.pi / 3)

# 20 - 5π/6 rad = 150°
confere(20, math.degrees(5 * math.pi / 6), 150.0)

# 21 - sen(2x - π) = 0,5 nas soluções de [0, 2π): 7π/12, 11π/12, 19π/12, 23π/12
for k in (7, 11, 19, 23):
    confere(21, math.sin(2 * (k * math.pi / 12) - math.pi), 0.5)

# 22 - f(x) = sen(3x - π): período 2π/3 e amplitude 1
f = lambda x: math.sin(3 * x - math.pi)
amostras = [i / 1000 for i in range(7000)]
confere(22, all(math.isclose(f(t + 2 * math.pi / 3), f(t), abs_tol=1e-9) for t in amostras), True)
confere(22, round(max(f(t) for t in amostras), 4), 1.0)
