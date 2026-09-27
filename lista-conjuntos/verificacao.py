"""
Lista de Exercícios - Teoria dos Conjuntos
Conferência em Python das questões que envolvem cálculo ou podem ser testadas com exemplos.
"""
from itertools import combinations, product


def confere(questao, obtido, esperado):
    assert obtido == esperado, f"Questão {questao}: obtido {obtido}, esperado {esperado}"
    print(f"Questão {questao:>2}: {obtido}  OK")


def subconjuntos(conjunto):
    elementos = sorted(conjunto)
    return [set(c) for k in range(len(elementos) + 1) for c in combinations(elementos, k)]


# 1 - cardinalidade
confere(1, len({1, 2, 3, 4, 5}), 5)

# 2 - nenhum natural fica estritamente entre 0 e 1
confere(2, [x for x in range(0, 100) if 0 < x < 1], [])

# 3 - subconjunto próprio: todo elemento de A está em B e A é diferente de B
confere(3, {1, 2} < {1, 2, 3}, True)

# 4 e 5 - união e interseção
A, B = {2, 4, 6}, {4, 6, 8, 10}
confere(4, sorted(A | B), [2, 4, 6, 8, 10])
confere(5, sorted(A & B), [4, 6])

# 6 a 8 - diferença e diferença simétrica
A, B = {1, 2, 3}, {3, 4, 5}
confere(6, sorted(B - A), [4, 5])
confere(7, (A ^ B) == (A | B) - (A & B), True)
confere(8, sorted(A ^ B), [1, 2, 4, 5])

# 9 - conjuntos disjuntos
A, B = {1, 2}, {7, 8}
confere(9, (A ^ B) == (A | B), True)

# 10 a 12 - inclusão-exclusão com 100 alunos
confere(10, len({1, 2, 3} | {3, 4}), len({1, 2, 3}) + len({3, 4}) - len({1, 2, 3} & {3, 4}))
pelo_menos_uma = 60 + 50 - 20
confere(11, pelo_menos_uma, 90)
confere(12, 100 - pelo_menos_uma, 10)

# 13 - regiões do diagrama de Venn com 4 conjuntos (padrões dentro/fora, exceto "fora de todos")
confere(13, sum(1 for padrao in product([0, 1], repeat=4) if any(padrao)), 15)

# 14 - INNER JOIN pelas chaves: só as chaves que existem nas duas tabelas
clientes = {101, 102, 103, 104}
clientes_com_pedido = {102, 104, 105}
confere(14, sorted(clientes & clientes_com_pedido), [102, 104])

# 15 - conjunto potência de um conjunto com 4 elementos
confere(15, len(subconjuntos({"a", "b", "c", "d"})), 16)

# 16 e 17 - produto cartesiano
A, B = ["x", "y"], [1, 2]
AxB = set(product(A, B))
BxA = set(product(B, A))
confere(16, sorted(AxB), [("x", 1), ("x", 2), ("y", 1), ("y", 2)])
confere(17, (AxB == BxA, len(AxB) == len(A) * len(B)), (False, True))

# 18, 19 e 22 a 24 - leis da álgebra de conjuntos, testadas em todos os pares de subconjuntos de U
U = {1, 2, 3, 4}
todos = subconjuntos(U)
pares = [(X, Y) for X in todos for Y in todos]
confere(18, all(U - (X & Y) == (U - X) | (U - Y) for X, Y in pares), True)
confere(19, all(X | (X & Y) == X for X, Y in pares), True)

# 20 e 21 - pares e ímpares formam uma partição dos naturais (testado de 0 a 99)
N = set(range(100))
T0 = {n for n in N if n % 2 == 0}
T1 = {n for n in N if n % 2 == 1}
confere(20, (T0 & T1 == set(), T0 | T1 == N), (True, True))
confere(21, len(T0) + len(T1) == len(N), True)

confere(22, all(X - Y == X & (U - Y) for X, Y in pares), True)
confere(23, all(X | (U - X) == U for X in todos), True)
confere(24, all(X & Y == Y & X for X, Y in pares), True)

# 25 - AND bit a bit como interseção: bit i ligado = elemento i presente
bits_A = 0b1100  # {2, 3}
bits_B = 0b1010  # {1, 3}
confere(25, bin(bits_A & bits_B), "0b1000")  # {3}

# 26 - |A ∩ B| = |A| + |B| - |A ∪ B|
confere(26, 10 + 15 - 20, 5)

# 27 - inclusão-exclusão com 3 conjuntos: a interseção tripla é somada
A, B, C = {1, 2, 3, 4}, {3, 4, 5}, {4, 5, 6}
formula = (len(A) + len(B) + len(C) - len(A & B) - len(A & C) - len(B & C) + len(A & B & C))
confere(27, formula, len(A | B | C))

# 28 - x mod 2 = 0 seleciona os pares, inclusive negativos e o zero
confere(28, [x for x in range(-6, 7) if x % 2 == 0], [-6, -4, -2, 0, 2, 4, 6])

# 29 - o set elimina duplicatas e tem & e |
confere(29, sorted(set([3, 1, 3, 2, 1])), [1, 2, 3])

# 30 - diferença simétrica vazia implica conjuntos iguais (testado em todos os pares)
confere(30, all(X == Y for X, Y in pares if not (X ^ Y)), True)
