# Aula 02 — Exercícios

Exercícios propostos no slide da Aula 02: operações com conjuntos, número de subconjuntos, princípio da inclusão-exclusão e o desafio prático de implementar um conjunto em Python.

As respostas dos exercícios 1 a 3 foram conferidas em [`verificacao.py`](verificacao.py).

## 1. Exercícios de fixação: conjuntos

IDs de alunos da Turma 1 cadastrados em diferentes módulos do sistema:

- **A** = {10, 15, 20, 25, 30} — matriculados em Sistemas de Informação
- **B** = {20, 30, 40, 50} — matriculados na disciplina de PI
- **C** = {10, 20} — alunos que já entregaram a documentação

| Operação | Significado | Resultado |
|---|---|---|
| A ∪ B | alunos cadastrados no sistema geral | {10, 15, 20, 25, 30, 40, 50} |
| A ∩ B | alunos do curso que cursam PI | {20, 30} |
| A \ B | alunos do curso que não cursam PI | {10, 15, 25} |
| (A ∪ B) \ C | alunos com documentação pendente | {15, 25, 30, 40, 50} |

- **União:** junta os IDs de A e de B. O 20 e o 30 aparecem nos dois, mas entram uma vez só — 7 alunos no sistema.
- **Interseção:** ficam só os IDs presentes nos dois conjuntos, 20 e 30.
- **Diferença A \ B:** retira de A os IDs que também estão em B (20 e 30) e sobram 10, 15 e 25.
- **(A ∪ B) \ C:** parte dos 7 alunos da união e retira quem já entregou a documentação (10 e 20), restando 5 alunos com pendência.

## 2. Número de subconjuntos

Um relatório cruza 5 tabelas (A, B, C, D e E) com JOINs.

**a) Número máximo de subconjuntos disjuntos formados pela interseção das 5 tabelas**

Cada registro pode estar ou não estar em cada tabela — 2 possibilidades por tabela:

$$2 \times 2 \times 2 \times 2 \times 2 = 2^5 = 32 \text{ combinações}$$

Uma dessas combinações é "não está em nenhuma tabela", que fica fora do diagrama e não é uma região do cruzamento. Portanto:

$$2^5 - 1 = 31 \text{ subconjuntos disjuntos}$$

**b) Novos subconjuntos ao adicionar uma 6ª tabela**

Com 6 tabelas: $2^6 - 1 = 63$ subconjuntos. Novos: $63 - 31 = 32$ **subconjuntos exclusivos**.

Outra forma de ver: as regiões novas são exatamente as que incluem a 6ª tabela. Ela pode ser combinada com qualquer escolha das 5 tabelas anteriores (inclusive nenhuma delas), o que dá $2^5 = 32$.

## 3. O princípio da inclusão-exclusão com 3 conjuntos

1232 estudantes cursaram Espanhol (E), 879 Francês (F) e 114 Russo (R); 103 cursaram Espanhol e Francês, 23 Espanhol e Russo e 14 Francês e Russo. Se 2092 cursaram pelo menos um dos três, quantos cursaram os três?

Somando os três cursos, quem fez dois cursos é contado duas vezes, por isso as interseções duplas são subtraídas; quem fez os três é somado três vezes e subtraído três vezes, então a interseção tripla precisa ser somada de volta:

$$|E \cup F \cup R| = |E| + |F| + |R| - |E \cap F| - |E \cap R| - |F \cap R| + |E \cap F \cap R|$$

Chamando de $x$ o número de estudantes nos três cursos:

$$2092 = 1232 + 879 + 114 - 103 - 23 - 14 + x$$

$$2092 = 2225 - 140 + x = 2085 + x \quad\Rightarrow\quad x = 7$$

**Resposta: 7 estudantes cursaram os três idiomas.**

## 4. Desafio prático: implementando conjuntos

Construir, sem usar o tipo `set` do Python, uma classe `MeuConjunto` que simule um conjunto matemático usando apenas listas.

- [`meu_conjunto_parte1.py`](meu_conjunto_parte1.py) — o construtor recebe uma lista e descarta os valores repetidos; `uniao(outro)` e `intersecao(outro)` devolvem um novo `MeuConjunto`.
- [`meu_conjunto_parte2.py`](meu_conjunto_parte2.py) — `uniao` e `intersecao` passam a aceitar vários conjuntos, como em `A.uniao(B, C, D, E)`, usando o parâmetro `*outros`.

A unicidade fica no método `adicionar`, que só insere um valor se ele ainda não estiver na lista. Tanto o construtor quanto a união passam por esse método, então nenhum resultado tem elementos repetidos. Na interseção com vários conjuntos, um valor só entra se estiver em **todos** eles (`all(...)`).

Saída da parte 2, usando os conjuntos A, B e C do exercício 1:

```
União de A e B: {10, 15, 20, 25, 30, 40, 50}
União de A, B e C: {10, 15, 20, 25, 30, 40, 50}
Interseção de A e B: {20, 30}
Interseção de A, B e C: {20}
União de D, E, F, G e H: {2, 4, 6, 8, 12, 1, 16, 9, 0}
Interseção de D, E, F, G e H: {4, 8}
```

Os resultados coincidem com o exercício 1: a união e a interseção de A e B são as mesmas calculadas à mão, e o único aluno que está nos três conjuntos é o de ID 20.
