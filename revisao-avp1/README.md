# Lista de Revisão — AVP1 (Conjuntos e Funções)

Resolução das 20 questões da lista de revisão para a AVP1. Cada questão traz o enunciado da lista e, em seguida, a resolução com os cálculos e a justificativa. Todas as respostas foram conferidas em Python no arquivo [`verificacao.py`](verificacao.py).

> **Orientações da lista:** resolva as questões apresentando os cálculos e justificando suas respostas. Os exercícios retomam os conteúdos trabalhados nas aulas.

## Respostas

| Questão | Resposta |
|---|---|
| 1 | A ∪ B = {10, 15, 20, 25, 30, 40, 50}; A ∩ B = {20, 30}; A \ B = {10, 15, 25} |
| 2 | complementar de A em U = {3, 6, 8, 10} |
| 3 | B \ A, que pode ser reescrita como B ∩ Aᶜ |
| 4 | pelo menos uma: {1, 2, 3, 4, 5, 7, 8, 9}; as duas: {2, 3, 7}; apenas uma: {1, 4, 5, 8, 9} |
| 5 | raiz x = 4 |
| 6 | C(g) = 100 + 0,02g; 5.000 GB custam R$ 200,00; R$ 300,00 correspondem a 10.000 GB |
| 7 | inicial 28 graus; taxa de −2 graus por hora; chega a zero em t = 14 h |
| 8 | custos iguais em x = 30; para x = 10, B é mais barato; para x = 40, A é mais barato |
| 9 | s(t) = 5t + 5; s(12) = 65 m |
| 10 | variação vertical de 100√3 ≈ 173,2 |
| 11 | raízes 3 e 7; lucro positivo para 3 < x < 7 e negativo para x < 3 ou x > 7 |
| 12 | altura máxima de 22 em t = 2 |
| 13 | V(4, 42): receita máxima de R$ 42 mil com 400 produtos |
| 14 | domínio ℝ − {2}; assíntota vertical x = 2 |
| 15 | x = 3 não pode ser usado; perto de 3 a função cresce sem limite (assíntota x = 3) |
| 16 | M(3) = R$ 5.324,00 |
| 17 | t ≈ 9,7 anos |
| 18 | x = 64, com a condição x > 0 |
| 19 | altura mínima 1, máxima 9 e período 4 |
| 20 | m = √3/3 ≈ 0,577; variação vertical de 100√3 ≈ 173,2; ângulo maior deixa a trajetória mais inclinada |

## Conjuntos

### Questão 1
> **Enunciado:** Uma plataforma de comércio eletrônico analisou dois conjuntos de usuários:
>
> A = {10, 15, 20, 25, 30}, B = {20, 30, 40, 50}.
>
> Determine A ∪ B, A ∩ B e A \ B. Explique o significado de cada resultado no contexto do problema.

**Resolução:**

| Operação | Resultado | Significado |
|---|---|---|
| A ∪ B | {10, 15, 20, 25, 30, 40, 50} | usuários que aparecem em pelo menos um dos dois grupos analisados |
| A ∩ B | {20, 30} | usuários que estão nos dois grupos ao mesmo tempo |
| A \ B | {10, 15, 25} | usuários que estão no grupo A, mas não no grupo B |

A união tem 7 usuários, e não 9 (5 + 4), porque o 20 e o 30 estão nos dois grupos e só podem ser contados uma vez:

$$|A \cup B| = |A| + |B| - |A \cap B| = 5 + 4 - 2 = 7$$

### Questão 2
> **Enunciado:** Uma empresa possui um banco de dados com todos os usuários ativos:
>
> U = {1, 2, 3, …, 10}.
>
> O conjunto A contém os usuários que utilizaram o aplicativo no último mês:
>
> A = {1, 2, 4, 5, 7, 9}.
>
> Determine o complementar de A em U e interprete o resultado.

**Resolução:**

O complementar reúne os elementos do universo que não estão em A:

**Aᶜ = U − A = {3, 6, 8, 10}**

**Interpretação:** são os 4 usuários ativos que **não** usaram o aplicativo no último mês — 40% da base. Esse é o público de uma campanha para trazê-los de volta ao aplicativo. Conferência: $|A| + |A^c| = 6 + 4 = 10 = |U|$.

### Questão 3
> **Enunciado:** Em uma pesquisa, A representa os clientes que utilizaram um serviço e B os que utilizaram um segundo serviço. Explique, usando operações de conjuntos, qual expressão representa os clientes que utilizaram o segundo serviço, mas não o primeiro. Mostre também como essa operação pode ser reescrita usando o complementar e a interseção.

**Resolução:**

Quem usou o segundo serviço e não o primeiro está em $B$ e fora de $A$. Isso é a **diferença** $B \setminus A$ (também escrita $B - A$).

Estar fora de $A$ é o mesmo que estar no complementar de $A$, então:

$$x \in B \setminus A \iff x \in B \text{ e } x \notin A \iff x \in B \text{ e } x \in A^c \iff x \in B \cap A^c$$

$$B \setminus A = B \cap A^c$$

A ordem importa: $A \setminus B = A \cap B^c$ seriam os clientes que usaram o primeiro serviço e não o segundo.

*Exemplo:* com U = {1, 2, 3, 4, 5, 6}, A = {1, 2, 3} e B = {2, 3, 4, 5}, temos B \ A = {4, 5}, Aᶜ = {4, 5, 6} e B ∩ Aᶜ = {4, 5} — o mesmo conjunto.

### Questão 4
> **Enunciado:** Em uma universidade,
>
> P = {1, 2, 3, 5, 7, 8}, D = {2, 3, 4, 7, 9},
>
> onde P representa estudantes de uma oficina de programação e D os de uma oficina de análise de dados. Determine os estudantes que participaram de pelo menos uma oficina, os que participaram das duas e os que participaram de apenas uma.

**Resolução:**

- **Pelo menos uma oficina** — união: P ∪ D = {1, 2, 3, 4, 5, 7, 8, 9}, ou seja, **8 estudantes**.
- **As duas oficinas** — interseção: P ∩ D = {2, 3, 7}, ou seja, **3 estudantes**.
- **Apenas uma oficina** — diferença simétrica, a união sem a interseção: (P ∪ D) − (P ∩ D) = {1, 4, 5, 8, 9}, ou seja, **5 estudantes**. Destes, {1, 5, 8} fizeram só programação (P − D) e {4, 9} só análise de dados (D − P).

Conferência pela inclusão-exclusão: $|P \cup D| = 6 + 5 - 3 = 8$, que também é a soma de quem fez as duas com quem fez apenas uma: $3 + 5 = 8$.

## Função afim

### Questão 5
> **Enunciado:** Considere
>
> $$f(x) = 3x - 12.$$
>
> Uma empresa utiliza essa função para representar uma grandeza em função de $x$. Determine a raiz da função e explique o significado de uma raiz no contexto de um modelo aplicado.

**Resolução:**

$$f(x) = 0 \quad\Rightarrow\quad 3x - 12 = 0 \quad\Rightarrow\quad x = 4$$

A raiz é o valor de $x$ em que a grandeza modelada vale **zero** — o ponto em que o gráfico corta o eixo x. Como o coeficiente angular é positivo ($a = 3$), a grandeza é negativa para $x < 4$ e positiva para $x > 4$; a raiz marca a mudança de sinal. Se $f$ representasse o lucro em função das unidades vendidas, por exemplo, $x = 4$ seria o **ponto de equilíbrio**: abaixo de 4 unidades há prejuízo e acima há lucro.

### Questão 6
> **Enunciado:** Uma empresa de armazenamento em nuvem cobra R\$100,00 de taxa fixa mais R\$0,02 por GB armazenado. Determine a função $C(g)$, calcule o custo de 5.000 GB e determine quantos GB correspondem a uma cobrança de R\$300,00.

**Resolução:**

A taxa fixa é o coeficiente linear e o preço por GB é o coeficiente angular:

$$C(g) = 100 + 0{,}02g$$

- **5.000 GB:** $C(5000) = 100 + 0{,}02 \cdot 5000 = 100 + 100 = 200$, ou seja, **R\$ 200,00**.
- **Cobrança de R\$ 300,00:**

$$100 + 0{,}02g = 300 \quad\Rightarrow\quad 0{,}02g = 200 \quad\Rightarrow\quad g = \frac{200}{0{,}02} = 10.000 \text{ GB}$$

Dobrar o armazenamento de 5.000 para 10.000 GB não dobra a conta (de R\$ 200 para R\$ 300), por causa da taxa fixa.

### Questão 7
> **Enunciado:** Um sensor de temperatura apresenta
>
> $$T(t) = -2t + 28,$$
>
> em que $t$ é o tempo em horas. Determine a temperatura inicial, a taxa de variação e o instante em que a temperatura prevista pelo modelo chega a zero. Explique o que o sinal do coeficiente angular indica.

**Resolução:**

- **Temperatura inicial:** $T(0) = 28$ graus.
- **Taxa de variação:** é o coeficiente angular, $-2$: a temperatura cai **2 graus por hora**.
- **Temperatura zero:** $-2t + 28 = 0 \Rightarrow t = 14$ horas.
- **Sinal do coeficiente angular:** negativo, então a função é **decrescente** — a temperatura diminui com o passar do tempo. Um coeficiente positivo indicaria aquecimento, e um coeficiente zero, temperatura constante.

### Questão 8
> **Enunciado:** Dois serviços possuem custos
>
> $$A(x) = 50 + 4x, \qquad B(x) = 20 + 5x.$$
>
> Determine a quantidade $x$ para a qual os custos são iguais. Depois, determine qual serviço é mais barato para $x = 10$ e para $x = 40$.

**Resolução:**

$$50 + 4x = 20 + 5x \quad\Rightarrow\quad 30 = x$$

Para $x = 30$ os dois custam $A(30) = B(30) = 170$.

| x | A(x) | B(x) | Mais barato |
|---|---|---|---|
| 10 | 50 + 40 = 90 | 20 + 50 = 70 | **B** |
| 40 | 50 + 160 = 210 | 20 + 200 = 220 | **A** |

O serviço B tem taxa fixa menor (20 contra 50), mas custa mais por unidade (5 contra 4). Até $x = 30$ a taxa fixa menor pesa mais e B sai mais barato; acima de 30, o custo por unidade menor de A compensa a taxa fixa maior.

### Questão 9
> **Enunciado:** A posição de um personagem é modelada por uma função linear. Em $t = 2$ segundos ele está em 15 metros e, em $t = 8$ segundos, em 45 metros. Determine a função posição e calcule a posição em $t = 12$ segundos.

**Resolução:**

O coeficiente angular é a velocidade, a variação da posição dividida pela variação do tempo:

$$v = \frac{45 - 15}{8 - 2} = \frac{30}{6} = 5 \text{ m/s}$$

Com $s(t) = 5t + b$ e o ponto $(2, 15)$: $15 = 5 \cdot 2 + b \Rightarrow b = 5$ (a posição em $t = 0$).

$$s(t) = 5t + 5$$

Conferência: $s(8) = 40 + 5 = 45$. Em $t = 12$: $s(12) = 60 + 5 = 65$, ou seja, **65 m**.

### Questão 10
> **Enunciado:** Em um jogo, a trajetória de um tiro é uma reta que forma um ângulo de 30° com a horizontal. O projétil parte de $x = 100$ e atinge um alvo em $x = 400$. Sabendo que
>
> $$\tan 30^\circ = \frac{\sqrt{3}}{3},$$
>
> determine a variação vertical entre o disparo e o alvo. Relacione o resultado ao coeficiente angular da função linear.

**Resolução:**

A variação horizontal é $\Delta x = 400 - 100 = 300$. Em uma reta, a tangente do ângulo de inclinação é a razão entre a variação vertical e a horizontal:

$$\tan 30^\circ = \frac{\Delta y}{\Delta x} \quad\Rightarrow\quad \Delta y = 300 \cdot \frac{\sqrt{3}}{3} = 100\sqrt{3} \approx 173{,}2$$

**Relação com o coeficiente angular:** o coeficiente angular da reta é exatamente $m = \tan 30^\circ = \frac{\sqrt{3}}{3} \approx 0{,}577$. Ele diz quanto o projétil sobe para cada unidade percorrida na horizontal, e a variação vertical é esse valor multiplicado pela distância horizontal: $\Delta y = m \cdot \Delta x$.

## Função quadrática

### Questão 11
> **Enunciado:** O lucro de uma empresa é modelado por
>
> $$L(x) = -x^2 + 10x - 21.$$
>
> Determine as raízes e os intervalos em que o lucro é positivo e negativo.

**Resolução:**

$$\Delta = 10^2 - 4(-1)(-21) = 100 - 84 = 16 \qquad x = \frac{-10 \pm 4}{-2} \quad\Rightarrow\quad x_1 = 3,\ \ x_2 = 7$$

Na forma fatorada, $L(x) = -(x - 3)(x - 7)$. Como $a = -1 < 0$, a parábola tem concavidade para baixo, então fica **acima** do eixo x entre as raízes e **abaixo** fora delas:

| x | x < 3 | x = 3 | 3 < x < 7 | x = 7 | x > 7 |
|---|---|---|---|---|---|
| L(x) | negativo | 0 | **positivo** | 0 | negativo |

- **Lucro positivo:** $3 < x < 7$.
- **Lucro negativo (prejuízo):** $x < 3$ ou $x > 7$.

O maior lucro acontece no vértice, no meio das raízes: $x_V = 5$, com $L(5) = -25 + 50 - 21 = 4$.

### Questão 12
> **Enunciado:** Um objeto lançado em um jogo segue
>
> $$h(t) = -5t^2 + 20t + 2.$$
>
> Determine o instante em que atinge a altura máxima e o valor dessa altura. Explique como o sinal do coeficiente de $t^2$ influencia a trajetória.

**Resolução:**

$$t_V = -\frac{b}{2a} = -\frac{20}{2 \cdot (-5)} = 2 \qquad h(2) = -5 \cdot 4 + 20 \cdot 2 + 2 = -20 + 40 + 2 = 22$$

O objeto atinge a **altura máxima de 22** no instante **t = 2**. Ele parte da altura $h(0) = 2$.

**Sinal do coeficiente de $t^2$:** é negativo ($-5$), então a parábola tem concavidade para baixo — o objeto sobe, para no vértice e depois desce, como um lançamento real sob a gravidade. Se esse coeficiente fosse positivo, a concavidade seria para cima: a função teria um ponto de **mínimo** e cresceria sem parar, o que não descreve um objeto lançado.

### Questão 13
> **Enunciado:** Uma empresa modela sua receita, em milhares de reais, por
>
> $$R(x) = -2x^2 + 16x + 10,$$
>
> em que $x$ representa centenas de produtos vendidos. Determine o vértice e interprete seus valores. Para qual quantidade de produtos ocorre a receita máxima?

**Resolução:**

$$x_V = -\frac{b}{2a} = -\frac{16}{2 \cdot (-2)} = 4 \qquad y_V = R(4) = -2 \cdot 16 + 16 \cdot 4 + 10 = -32 + 64 + 10 = 42$$

O vértice é $V(4, 42)$. Como $a = -2 < 0$, ele é o ponto de **máximo**:

- $x_V = 4$ centenas, ou seja, **400 produtos** vendidos;
- $y_V = 42$ milhares, ou seja, **receita máxima de R\$ 42.000,00**.

Neste modelo, vender mais de 400 produtos faz a receita diminuir.

## Função racional

### Questão 14
> **Enunciado:** Um sistema de monitoramento utiliza
>
> $$T(x) = \frac{10}{x - 2}.$$
>
> Determine o domínio e a assíntota vertical. Explique por que $x = 2$ não pode pertencer ao domínio.

**Resolução:**

O denominador não pode ser zero: $x - 2 \neq 0 \Rightarrow x \neq 2$.

- **Domínio:** todos os reais exceto 2, ou seja, ℝ − {2}.
- **Assíntota vertical:** a reta $x = 2$.

**Por que $x = 2$ fica fora:** com $x = 2$ a conta seria $\frac{10}{0}$, e a divisão por zero não está definida — não existe número que, multiplicado por 0, dê 10. Perto de 2, o denominador fica muito pequeno e o valor da função dispara:

| x | 1,9 | 1,99 | 2,01 | 2,1 |
|---|---|---|---|---|
| T(x) | −100 | −1000 | 1000 | 100 |

Por isso o gráfico se aproxima da reta $x = 2$ sem nunca tocá-la: quando $x$ se aproxima de 2 pela direita, $T(x) \to +\infty$; pela esquerda, $T(x) \to -\infty$.

### Questão 15
> **Enunciado:** Uma empresa modela um indicador por
>
> $$R(x) = \frac{x + 4}{x - 3}.$$
>
> Determine o valor que não pode ser utilizado para $x$ e explique o que ocorre com a função quando $x$ se aproxima desse valor.

**Resolução:**

O valor proibido é **x = 3**, que zera o denominador.

Quando $x$ se aproxima de 3, o numerador se aproxima de $3 + 4 = 7$ (não zero) e o denominador se aproxima de 0. Um número próximo de 7 dividido por um número cada vez menor fica cada vez maior em módulo:

| x | 2,9 | 2,99 | 3,01 | 3,1 |
|---|---|---|---|---|
| R(x) | −69 | −699 | 701 | 71 |

- Pela direita ($x > 3$), o denominador é positivo e $R(x) \to +\infty$.
- Pela esquerda ($x < 3$), o denominador é negativo e $R(x) \to -\infty$.

A função não tem valor em $x = 3$ e possui ali uma **assíntota vertical**: o indicador "explode" e o modelo deixa de fazer sentido perto desse valor.

## Função exponencial e logarítmica

### Questão 16
> **Enunciado:** Um investimento inicial de R\$4.000,00 rende juros compostos de 10% ao ano:
>
> $$M(t) = 4000(1{,}10)^t.$$
>
> Determine o montante após 3 anos e explique por que o modelo é exponencial e não linear.

**Resolução:**

$$M(3) = 4000 \cdot 1{,}10^3 = 4000 \cdot 1{,}331 = 5324$$

O montante após 3 anos é **R\$ 5.324,00**.

**Por que é exponencial:** a variável $t$ está no **expoente**. A cada ano o valor é multiplicado por 1,10, então os juros incidem sobre os juros dos anos anteriores e o acréscimo anual aumenta:

| Ano | Montante | Acréscimo no ano |
|---|---|---|
| 0 | R\$ 4.000,00 | — |
| 1 | R\$ 4.400,00 | R\$ 400,00 |
| 2 | R\$ 4.840,00 | R\$ 440,00 |
| 3 | R\$ 5.324,00 | R\$ 484,00 |

Em um modelo linear, o acréscimo seria sempre o mesmo — com juros simples, por exemplo, seriam R\$ 400,00 por ano e R\$ 5.200,00 após 3 anos. Razão constante entre anos seguidos caracteriza a função exponencial; diferença constante caracteriza a função linear.

### Questão 17
> **Enunciado:** Um investimento de R\$5.000,00 cresce a juros compostos de 12% ao ano. Determine quando ele atingirá R\$15.000,00. Monte a equação e use logaritmos, considerando
>
> $$\log 3 \approx 0{,}4771, \qquad \log 1{,}12 \approx 0{,}0492.$$

**Resolução:**

$$5000 \cdot 1{,}12^t = 15000 \quad\Rightarrow\quad 1{,}12^t = 3$$

Aplicando logaritmo dos dois lados e a propriedade $\log(a^t) = t \log a$:

$$t \cdot \log 1{,}12 = \log 3 \quad\Rightarrow\quad t = \frac{\log 3}{\log 1{,}12} \approx \frac{0{,}4771}{0{,}0492} \approx 9{,}7 \text{ anos}$$

O investimento atinge R\$ 15.000,00 em cerca de **9,7 anos** (aproximadamente 9 anos e 8 meses). Se os juros forem creditados só no fim de cada ano, o valor é ultrapassado no 10º ano: após 9 anos o montante é de cerca de R\$ 13.865,39 e após 10 anos, R\$ 15.529,24.

### Questão 18
> **Enunciado:** Um sistema utiliza a função
>
> $$f(x) = \log_2(x).$$
>
> Determine $x$ quando $f(x) = 6$ e indique a condição que $x$ deve satisfazer para que o logaritmo esteja definido.

**Resolução:**

Pela definição de logaritmo, $\log_2 x = 6$ significa que 2 elevado a 6 dá $x$:

$$x = 2^6 = 64$$

**Condição:** o logaritmando precisa ser positivo, $x > 0$ (a base 2 já é positiva e diferente de 1). Como 64 > 0, a solução é válida.

## Função trigonométrica

### Questão 19
> **Enunciado:** A altura de uma câmera que acompanha um personagem é
>
> $$h(t) = 5 + 4\,\text{sen}\left(\frac{\pi t}{2}\right).$$
>
> Determine a altura mínima, a altura máxima e o período do movimento. Explique o papel da amplitude na função.

**Resolução:**

O seno sempre fica entre $-1$ e $1$:

- **Altura mínima:** $5 + 4 \cdot (-1) = 1$, quando o seno vale $-1$ (em $t = 3$).
- **Altura máxima:** $5 + 4 \cdot 1 = 9$, quando o seno vale $1$ (em $t = 1$).
- **Período:**

$$T = \frac{2\pi}{\pi/2} = 4$$

O movimento se repete a cada 4 unidades de tempo.

**Papel da amplitude:** a amplitude é o 4 que multiplica o seno. Ela diz quanto a câmera se afasta da altura central 5, para cima e para baixo: vai de $5 - 4 = 1$ até $5 + 4 = 9$. Também pode ser calculada como (máxima − mínima)/2 = (9 − 1)/2 = 4. Uma amplitude 2, por exemplo, faria a câmera oscilar só entre 3 e 7. Na função, o 5 define a altura central, a amplitude define o tamanho da oscilação e o $\frac{\pi}{2}$ dentro do seno define a rapidez (o período).

## Função afim e trigonometria

### Questão 20
> **Enunciado:** Um personagem dispara um projétil em uma trajetória retilínea. O disparo ocorre em $x = 100$ e o alvo em $x = 400$, enquanto a trajetória forma um ângulo de 30° com a horizontal.
>
> (a) Determine o coeficiente angular da reta.
>
> (b) Determine a variação vertical entre o disparo e o alvo.
>
> (c) Explique o que aconteceria com a inclinação da trajetória se o ângulo de disparo aumentasse.

**Resolução:**

**(a) Coeficiente angular da reta**

O coeficiente angular é a tangente do ângulo de inclinação:

$$m = \tan 30^\circ = \frac{\sqrt{3}}{3} \approx 0{,}577$$

**(b) Variação vertical entre o disparo e o alvo**

$$\Delta y = m \cdot \Delta x = \frac{\sqrt{3}}{3} \cdot (400 - 100) = 100\sqrt{3} \approx 173{,}2$$

**(c) O que acontece se o ângulo de disparo aumentar**

Entre 0° e 90°, a tangente cresce junto com o ângulo. Um ângulo maior dá um coeficiente angular maior e uma trajetória **mais inclinada**: para a mesma distância horizontal de 300, o projétil sobe mais.

| Ângulo | Coeficiente angular | Variação vertical (Δx = 300) |
|---|---|---|
| 30° | √3/3 ≈ 0,577 | 100√3 ≈ 173,2 |
| 45° | 1 | 300 |
| 60° | √3 ≈ 1,732 | 300√3 ≈ 519,6 |

Perto de 90°, a tangente cresce sem limite e a trajetória fica quase vertical. Uma reta vertical já não seria uma função de $x$.
