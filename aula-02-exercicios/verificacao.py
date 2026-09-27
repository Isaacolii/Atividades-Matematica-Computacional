"""Aula 02 - conferência em Python das respostas dos exercícios 1 a 3."""
from itertools import product


def confere(item, obtido, esperado):
    assert obtido == esperado, f"{item}: obtido {obtido}, esperado {esperado}"
    print(f"{item}: {obtido}  OK")


# Exercício 1 - operações com os conjuntos de IDs
A = {10, 15, 20, 25, 30}
B = {20, 30, 40, 50}
C = {10, 20}

confere("1.1 União de A e B", sorted(A | B), [10, 15, 20, 25, 30, 40, 50])
confere("1.2 Interseção de A e B", sorted(A & B), [20, 30])
confere("1.3 A menos B", sorted(A - B), [10, 15, 25])
confere("1.4 (A união B) menos C", sorted((A | B) - C), [15, 25, 30, 40, 50])


# Exercício 2 - cada região do diagrama é um padrão "está / não está" em cada tabela;
# o padrão em que o registro não está em nenhuma tabela fica de fora
def regioes(n_tabelas):
    return sum(1 for padrao in product([False, True], repeat=n_tabelas) if any(padrao))


confere("2.1 Regiões com 5 tabelas", regioes(5), 31)
confere("2.2 Regiões novas com a 6ª tabela", regioes(6) - regioes(5), 32)

# Exercício 3 - inclusão-exclusão: |E ∪ F ∪ R| = soma simples - interseções duplas + tripla
soma_simples = 1232 + 879 + 114
soma_duplas = 103 + 23 + 14
tripla = 2092 - (soma_simples - soma_duplas)
confere("3 Cursaram os três idiomas", tripla, 7)
