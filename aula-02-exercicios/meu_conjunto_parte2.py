"""
Aula 02 - Desafio prático: implementando conjuntos (parte 2)

Complemento da parte 1: uniao e intersecao passam a aceitar vários conjuntos de uma vez,
por exemplo A.uniao(B, C) ou A.intersecao(B, C, D, E).
O parâmetro *outros recebe quantos conjuntos forem passados, como uma tupla.
"""


class MeuConjunto:
    def __init__(self, valores=None):
        self.elementos = []
        for valor in valores or []:
            self.adicionar(valor)

    def adicionar(self, valor):
        if not self.contem(valor):
            self.elementos.append(valor)

    def contem(self, valor):
        return valor in self.elementos

    def uniao(self, *outros):
        # Começa com uma cópia deste conjunto e acrescenta os elementos de cada um dos outros
        resultado = MeuConjunto(self.elementos)
        for conjunto in outros:
            for valor in conjunto.elementos:
                resultado.adicionar(valor)
        return resultado

    def intersecao(self, *outros):
        # Um elemento fica no resultado só se estiver em todos os conjuntos
        resultado = MeuConjunto()
        for valor in self.elementos:
            if all(conjunto.contem(valor) for conjunto in outros):
                resultado.adicionar(valor)
        return resultado

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        return "{" + ", ".join(str(valor) for valor in self.elementos) + "}"


if __name__ == "__main__":
    # IDs de alunos do exercício 1 da Aula 02
    A = MeuConjunto([10, 15, 20, 25, 30])  # matriculados em Sistemas de Informação
    B = MeuConjunto([20, 30, 40, 50])      # matriculados em PI
    C = MeuConjunto([10, 20])              # já entregaram a documentação

    print("União de A e B:", A.uniao(B))
    print("União de A, B e C:", A.uniao(B, C))
    print("Interseção de A e B:", A.intersecao(B))
    print("Interseção de A, B e C:", A.intersecao(B, C))

    # Cinco conjuntos de uma vez
    D = MeuConjunto([2, 4, 6, 8])
    E = MeuConjunto([4, 8, 12])
    F = MeuConjunto([1, 2, 4, 8, 16])
    G = MeuConjunto([4, 8, 9])
    H = MeuConjunto([0, 4, 8])
    print("União de D, E, F, G e H:", D.uniao(E, F, G, H))
    print("Interseção de D, E, F, G e H:", D.intersecao(E, F, G, H))
