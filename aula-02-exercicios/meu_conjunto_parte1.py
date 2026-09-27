"""
Aula 02 - Desafio prático: implementando conjuntos (parte 1)

Classe que simula um conjunto matemático usando apenas listas, sem o tipo set do Python:
- o construtor recebe uma lista de valores e descarta os repetidos (unicidade);
- uniao(outro) devolve um novo MeuConjunto com os elementos dos dois conjuntos;
- intersecao(outro) devolve um novo MeuConjunto só com os elementos em comum.
"""


class MeuConjunto:
    def __init__(self, valores=None):
        self.elementos = []
        for valor in valores or []:
            self.adicionar(valor)

    def adicionar(self, valor):
        # Um valor só entra se ainda não fizer parte do conjunto
        if not self.contem(valor):
            self.elementos.append(valor)

    def contem(self, valor):
        return valor in self.elementos

    def uniao(self, outro):
        resultado = MeuConjunto(self.elementos)
        for valor in outro.elementos:
            resultado.adicionar(valor)
        return resultado

    def intersecao(self, outro):
        resultado = MeuConjunto()
        for valor in self.elementos:
            if outro.contem(valor):
                resultado.adicionar(valor)
        return resultado

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        return "{" + ", ".join(str(valor) for valor in self.elementos) + "}"


if __name__ == "__main__":
    A = MeuConjunto([1, 2, 2, 3, 3, 3])
    B = MeuConjunto([3, 4, 5, 5])

    print("A =", A, "| cardinalidade:", len(A))
    print("B =", B, "| cardinalidade:", len(B))
    print("União de A e B:", A.uniao(B))
    print("Interseção de A e B:", A.intersecao(B))
    print("Interseção de A com {7, 8}:", A.intersecao(MeuConjunto([7, 8])))
