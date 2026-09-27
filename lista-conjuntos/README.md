# Lista de Exercícios — Teoria dos Conjuntos

Resolução das 30 questões de múltipla escolha. Primeiro vem o gabarito; depois, cada questão com a justificativa. As questões com cálculo, e as leis que podem ser testadas com exemplos, foram conferidas em [`verificacao.py`](verificacao.py).

## Gabarito

| Questão | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Resposta** | B | D | B | B | A | C | A | C | D | C |

| Questão | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Resposta** | A | A | C | C | D | C | C | B | C | B |

| Questão | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Resposta** | A | B | B | B | C | B | B | D | D | C |

## Conceitos básicos

**Questão 1.** Seja A = {1, 2, 3, 4, 5}. Qual é a cardinalidade de A?

**Resposta: B (5).** A cardinalidade |A| é o número de elementos distintos do conjunto, e A tem 5.

**Questão 2.** Qual alternativa representa A = {x ∈ ℕ | 0 < x < 1}?

**Resposta: D (A = ∅).** Não existe número natural estritamente entre 0 e 1 — depois do 0 vem o 1. O 0,5 satisfaz a desigualdade, mas não é natural. Nenhum elemento atende à propriedade, então o conjunto é vazio.

**Questão 3.** O que significa A ⊂ B (A é subconjunto próprio de B)?

**Resposta: B.** Todo elemento de A está em B e existe pelo menos um elemento de B fora de A — ou seja, A ⊆ B e A ≠ B. Exemplo: {1, 2} ⊂ {1, 2, 3}.

## Operações

**Questão 4.** Com A = {2, 4, 6} e B = {4, 6, 8, 10}, qual é A ∪ B?

**Resposta: B ({2, 4, 6, 8, 10}).** A união reúne os elementos dos dois conjuntos. O 4 e o 6 estão nos dois, mas em um conjunto cada elemento aparece uma vez só — por isso a alternativa D, com repetições, não está na forma correta.

**Questão 5.** Com os mesmos conjuntos, qual é A ∩ B?

**Resposta: A ({4, 6}).** São os únicos elementos que pertencem aos dois conjuntos.

**Questão 6.** Com A = {1, 2, 3} e B = {3, 4, 5}, qual é B − A?

**Resposta: C ({4, 5}).** B − A são os elementos de B que não estão em A: retirando o 3, sobram 4 e 5. A ordem importa — A − B seria {1, 2}.

**Questão 7.** Qual fórmula é equivalente à diferença simétrica A ⊖ B?

**Resposta: A ((A ∪ B) − (A ∩ B)).** A diferença simétrica reúne os elementos que estão em exatamente um dos conjuntos: tudo o que está na união, menos o que está nos dois. Também pode ser escrita como (A − B) ∪ (B − A).

**Questão 8.** Com A = {1, 2, 3} e B = {3, 4, 5}, qual é A ⊖ B?

**Resposta: C ({1, 2, 4, 5}).** A ∪ B = {1, 2, 3, 4, 5} e A ∩ B = {3}; retirando o 3 da união, fica {1, 2, 4, 5}.

**Questão 9.** Se A e B são disjuntos (A ∩ B = ∅), A ⊖ B é igual a:

**Resposta: D (A ∪ B).** A ⊖ B = (A ∪ B) − (A ∩ B) = (A ∪ B) − ∅ = A ∪ B. Sem elementos em comum, todo elemento da união está em exatamente um dos conjuntos.

## Contagem e inclusão-exclusão

**Questão 10.** Pelo princípio da inclusão-exclusão, |A ∪ B| é calculado por:

**Resposta: C (|A| + |B| − |A ∩ B|).** Ao somar |A| + |B|, cada elemento da interseção é contado duas vezes; subtrair |A ∩ B| uma vez faz com que todos sejam contados uma única vez.

**Questão 11.** Dos 100 alunos de SI, 60 programam em Python, 50 em Java e 20 nas duas. Quantos programam em pelo menos uma?

**Resposta: A (90).** |P ∪ J| = |P| + |J| − |P ∩ J| = 60 + 50 − 20 = 90.

**Questão 12.** No mesmo cenário, quantos não programam em nenhuma das duas?

**Resposta: A (10).** É o que sobra dos 100 alunos fora de P ∪ J: 100 − 90 = 10.

**Questão 13.** Qual é o número máximo de subconjuntos disjuntos gerados por n = 4 conjuntos em um diagrama de Venn?

**Resposta: C (15).** Cada região corresponde a uma escolha de "dentro" ou "fora" para cada um dos 4 conjuntos: 2⁴ = 16 combinações. Tirando a região que fica fora de todos, restam 16 − 1 = 15.

**Questão 14.** Em SQL, o INNER JOIN entre duas tabelas corresponde a qual operação de conjuntos?

**Resposta: C (interseção).** O INNER JOIN só devolve os registros cuja chave aparece nas duas tabelas, ou seja, as chaves comuns — como em A ∩ B.

**Questão 15.** Se |A| = 4, qual é a cardinalidade do conjunto potência P(A)?

**Resposta: D (16).** Para montar um subconjunto, cada um dos 4 elementos pode entrar ou não: |P(A)| = 2⁴ = 16, contando o vazio e o próprio A.

## Produto cartesiano

**Questão 16.** Qual é A × B para A = {x, y} e B = {1, 2}?

**Resposta: C ({(x, 1), (x, 2), (y, 1), (y, 2)}).** O produto cartesiano forma todos os pares ordenados (a, b) com a ∈ A e b ∈ B, sempre com o elemento de A na primeira posição: 2 · 2 = 4 pares.

**Questão 17.** Sobre o produto cartesiano, é correto afirmar que:

**Resposta: C.** O produto cartesiano não é comutativo, porque (x, 1) ≠ (1, x): trocar a ordem dos conjuntos troca a ordem dentro dos pares. A alternativa A é falsa pelo mesmo motivo; B é falsa porque |A × B| é o produto |A| · |B|, e não a soma; D descreve a interseção.

> Observação: a cardinalidade de A × B é |A| · |B|. Se a alternativa E, escrita como "|A||B|", significar esse produto, ela também é verdadeira. A alternativa C é a que descreve uma propriedade sem ambiguidade de escrita.

## Álgebra de conjuntos

**Questão 18.** Pela Lei de De Morgan, o complementar da interseção de dois conjuntos equivale a:

**Resposta: B (Ā ∪ B̄).** Um elemento não está em A ∩ B exatamente quando falta em pelo menos um dos dois — está fora de A **ou** fora de B. Logo, o complementar de A ∩ B é Ā ∪ B̄. A outra lei de De Morgan troca os papéis: o complementar de A ∪ B é Ā ∩ B̄.

**Questão 19.** Pela Lei da Absorção, A ∪ (A ∩ B) resulta em:

**Resposta: C (A).** A ∩ B já está contido em A, então juntá-lo a A não acrescenta nenhum elemento novo.

**Questão 20.** Que condições uma coleção de subconjuntos deve cumprir para ser uma partição de U?

**Resposta: B.** A união dos subconjuntos precisa ser U (cobrem tudo) e eles precisam ser disjuntos dois a dois (não se sobrepõem). Assim, cada elemento de U fica em exatamente um dos blocos.

**Questão 21.** Com U = ℕ, T0 (pares) e T1 (ímpares), {T0, T1} é partição de ℕ porque:

**Resposta: A (T0 ∩ T1 = ∅ e T0 ∪ T1 = ℕ).** Nenhum natural é par e ímpar ao mesmo tempo, e todo natural é um dos dois — exatamente as duas condições da questão 20.

**Questão 22.** Pela Lei da Diferença, A − B equivale a:

**Resposta: B (A ∩ B̄).** A − B são os elementos que estão em A e não estão em B, isto é, que estão em A e no complementar de B.

**Questão 23.** O que resulta de A ∪ Ā?

**Resposta: B (conjunto universo U).** Todo elemento de U está em A ou fora de A (em Ā), então juntar os dois dá o universo inteiro. Em comparação, A ∩ Ā = ∅.

**Questão 24.** Qual notação representa a Lei Comutativa da Interseção?

**Resposta: B (A ∩ B = B ∩ A).** Das outras: A é a associativa da união, C é a comutativa da união, D é a distributiva e E é a idempotência.

## Conjuntos na computação

**Questão 25.** Qual operador bitwise é o equivalente direto da interseção?

**Resposta: C (AND).** Se cada conjunto for representado por uma sequência de bits (bit 1 = elemento presente), o AND só deixa ligado o bit que está ligado nos dois — é a interseção. Exemplo: 1100 AND 1010 = 1000. Da mesma forma, OR corresponde à união e XOR à diferença simétrica.

**Questão 26.** Se |A| = 10, |B| = 15 e |A ∪ B| = 20, quanto vale |A ∩ B|?

**Resposta: B (5).** Pela inclusão-exclusão, 20 = 10 + 15 − |A ∩ B|, então |A ∩ B| = 25 − 20 = 5.

**Questão 27.** Na inclusão-exclusão para três conjuntos, a parcela |A ∩ B ∩ C| deve ser:

**Resposta: B (somada).** |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|. Um elemento que está nos três conjuntos é somado 3 vezes nas parcelas simples e subtraído 3 vezes nas interseções duplas, ficando com contagem zero. Somar |A ∩ B ∩ C| devolve a ele a contagem 1.

**Questão 28.** O que representa C = {x ∈ ℤ | x mod 2 = 0}?

**Resposta: D (todos os inteiros pares).** x mod 2 é o resto da divisão de x por 2; resto zero significa que x é divisível por 2. Isso vale para positivos, negativos e o zero: …, −4, −2, 0, 2, 4, …

**Questão 29.** Qual estrutura nativa do Python foi feita para conjuntos, elimina duplicatas e tem os operadores & e |?

**Resposta: D (set).** O `set` guarda cada elemento uma vez só e oferece `|` (união), `&` (interseção), `-` (diferença) e `^` (diferença simétrica).

**Questão 30.** Se A ⊖ B = ∅, o que se conclui obrigatoriamente sobre A e B?

**Resposta: C (A = B).**

*Prova.* Como A ⊖ B = (A − B) ∪ (B − A), se essa união é vazia, as duas partes são vazias:

- A − B = ∅ significa que nenhum elemento de A está fora de B, ou seja, A ⊆ B;
- B − A = ∅ significa, do mesmo modo, que B ⊆ A.

Com A ⊆ B e B ⊆ A, conclui-se que A = B. ∎

As outras alternativas não são obrigatórias: com A = B = {1}, temos A ⊖ B = ∅, mas os conjuntos não são disjuntos (A), nenhum é subconjunto próprio do outro (B) e eles não são vazios (E).
