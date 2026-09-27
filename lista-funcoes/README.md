# Lista de Revisão Geral — Funções

Resolução das 22 questões, divididas em função linear, quadrática, exponencial, logarítmica e trigonométricas. Todas as respostas foram conferidas em Python no arquivo [`verificacao.py`](verificacao.py).

## Respostas

| Questão | Resposta |
|---|---|
| 1 | m = −3/4; corta o eixo x em (1, 0) e o eixo y em (0, 3/4) |
| 2 | 5x + 4y − 13 = 0, ou y = −(5/4)x + 13/4 |
| 3 | y = √3·x + 2 − √3 |
| 4 | y = −x/3 |
| 5 | concavidade para cima; raízes 3 e 6; V(9/2, −9/4) |
| 6 | raiz dupla x = 3; V(3, 0) |
| 7 | f(x) = 5x² + 11 |
| 8 | f(x) = 3x² + 6x + 11 |
| 9 | 5⁵ = 3125 |
| 10 | x = −3/2 |
| 11 | x = 1/6 |
| 12 | 12.207.031 |
| 13 | decrescente; corta o eixo y em (0, 2) |
| 14 | −3/2 |
| 15 | log 15 = 1 − a + b |
| 16 | x = log 12 / log(8/9) ≈ −21,10 |
| 17 | domínio x > 1; raiz x = 2 |
| 18 | x = (1 + √5)/2 |
| 19 | 5π/3 rad |
| 20 | 150° |
| 21 | x = 7π/12 + kπ ou x = 11π/12 + kπ, com k inteiro |
| 22 | domínio ℝ; imagem [−1, 1]; período 2π/3; amplitude 1 |

## Função linear

### Questão 1
Determine o coeficiente angular e os pontos onde a reta $3x + 4y - 3 = 0$ cruza os eixos x e y.

Isolando $y$:

$$4y = -3x + 3 \quad\Rightarrow\quad y = -\frac{3}{4}x + \frac{3}{4}$$

- **Coeficiente angular:** $m = -\frac{3}{4}$ (a reta é decrescente).
- **Eixo x** (fazendo $y = 0$): $3x - 3 = 0 \Rightarrow x = 1$, ponto $(1, 0)$.
- **Eixo y** (fazendo $x = 0$): $4y - 3 = 0 \Rightarrow y = \frac{3}{4}$, ponto $(0, \frac{3}{4})$.

### Questão 2
Determine a equação da reta que passa por $P(1, 2)$ e $Q(-3, 7)$.

$$m = \frac{7 - 2}{-3 - 1} = \frac{5}{-4} = -\frac{5}{4}$$

Usando o ponto $P$ na forma ponto-inclinação:

$$y - 2 = -\frac{5}{4}(x - 1) \quad\Rightarrow\quad y = -\frac{5}{4}x + \frac{5}{4} + 2 = -\frac{5}{4}x + \frac{13}{4}$$

Multiplicando tudo por 4 e passando para um lado só: **$5x + 4y - 13 = 0$**.

Conferência com o ponto $Q$: $5(-3) + 4(7) - 13 = -15 + 28 - 13 = 0$.

### Questão 3
Determine a equação da reta com inclinação de 60° que passa por $P(1, 2)$.

O coeficiente angular é a tangente do ângulo de inclinação: $m = \tan 60^\circ = \sqrt{3}$.

$$y - 2 = \sqrt{3}(x - 1) \quad\Rightarrow\quad y = \sqrt{3}\,x + 2 - \sqrt{3}$$

Com valores aproximados: $y \approx 1{,}732x + 0{,}268$.

### Questão 4
Determine a reta perpendicular a $f(x) = 3x - 8$ que passa por $P(0, 0)$.

Duas retas são perpendiculares quando o produto dos coeficientes angulares é $-1$. Como a reta dada tem $m = 3$:

$$3 \cdot m_2 = -1 \quad\Rightarrow\quad m_2 = -\frac{1}{3}$$

A reta passa pela origem, então o coeficiente linear é zero: **$y = -\frac{1}{3}x$**.

## Função quadrática

### Questão 5
Determine a concavidade, as raízes e o vértice de $f(x) = x^2 - 9x + 18$.

- **Concavidade:** $a = 1 > 0$, então é voltada para cima.
- **Raízes:**

$$\Delta = (-9)^2 - 4 \cdot 1 \cdot 18 = 81 - 72 = 9 \qquad x = \frac{9 \pm 3}{2} \quad\Rightarrow\quad x_1 = 3,\ \ x_2 = 6$$

Conferência por soma e produto: $3 + 6 = 9 = -\frac{b}{a}$ e $3 \cdot 6 = 18 = \frac{c}{a}$.

- **Vértice:**

$$x_V = -\frac{b}{2a} = \frac{9}{2} \qquad y_V = -\frac{\Delta}{4a} = -\frac{9}{4}$$

$V\left(\frac{9}{2}, -\frac{9}{4}\right)$, ou $(4{,}5;\ -2{,}25)$. O $x_V$ fica exatamente no meio das raízes 3 e 6.

### Questão 6
Determine as raízes e o vértice de $f(x) = -3x^2 + 18x - 27$.

Colocando $-3$ em evidência, aparece um quadrado perfeito:

$$f(x) = -3(x^2 - 6x + 9) = -3(x - 3)^2$$

- **Raiz:** $x = 3$, raiz dupla. Confirma-se pelo discriminante: $\Delta = 18^2 - 4(-3)(-27) = 324 - 324 = 0$.
- **Vértice:** $V(3, 0)$. A parábola tem concavidade para baixo ($a = -3$) e só toca o eixo x no vértice, então 0 é o valor máximo da função.

### Questão 7
Determine a função do 2º grau que passa por $A(-1, 16)$, $B(0, 11)$ e $C(1, 16)$.

Substituindo os pontos em $f(x) = ax^2 + bx + c$:

- $B$: $f(0) = c = 11$
- $C$: $f(1) = a + b + 11 = 16 \Rightarrow a + b = 5$
- $A$: $f(-1) = a - b + 11 = 16 \Rightarrow a - b = 5$

Somando as duas últimas equações: $2a = 10$, então $a = 5$ e $b = 0$.

**$f(x) = 5x^2 + 11$**

Faz sentido que $b = 0$: os pontos $A$ e $C$ têm a mesma altura e estão à mesma distância de $x = 0$, então o eixo de simetria da parábola é o próprio eixo y.

### Questão 8
Determine a função do 2º grau com vértice $V(-1, 8)$ que passa por $P(-5, 56)$.

Pela forma canônica $f(x) = a(x - x_V)^2 + y_V$:

$$f(x) = a(x + 1)^2 + 8$$

Usando o ponto $P$:

$$56 = a(-5 + 1)^2 + 8 = 16a + 8 \quad\Rightarrow\quad a = 3$$

$$f(x) = 3(x + 1)^2 + 8 = 3(x^2 + 2x + 1) + 8 = 3x^2 + 6x + 11$$

Conferência do vértice: $x_V = -\frac{6}{2 \cdot 3} = -1$ e $f(-1) = 3 - 6 + 11 = 8$.

## Função exponencial

### Questão 9
Simplifique $5^3 \cdot 5^2$.

No produto de potências de mesma base, somam-se os expoentes:

$$5^3 \cdot 5^2 = 5^{3+2} = 5^5 = 3125$$

### Questão 10
Determine $x$ em $100^x = 0{,}001$.

Escrevendo os dois lados como potência de 10: $100 = 10^2$ e $0{,}001 = 10^{-3}$.

$$10^{2x} = 10^{-3} \quad\Rightarrow\quad 2x = -3 \quad\Rightarrow\quad x = -\frac{3}{2}$$

### Questão 11
Determine $x$ em $8^{2x-1} = 0{,}25$.

Com base 2: $8 = 2^3$ e $0{,}25 = \frac{1}{4} = 2^{-2}$.

$$2^{3(2x-1)} = 2^{-2} \quad\Rightarrow\quad 6x - 3 = -2 \quad\Rightarrow\quad x = \frac{1}{6}$$

### Questão 12
Determine o valor de $1 + 5 + 5^2 + \cdots + 5^{10}$.

É a soma de uma progressão geométrica com primeiro termo $a_1 = 1$, razão $q = 5$ e $n = 11$ termos (expoentes de 0 a 10):

$$S_n = a_1 \cdot \frac{q^n - 1}{q - 1} = \frac{5^{11} - 1}{5 - 1} = \frac{48\,828\,125 - 1}{4} = 12\,207\,031$$

### Questão 13
Determine a direção de crescimento e o ponto em que $f(x) = 2^{1-x}$ corta o eixo y.

$$f(x) = 2^{1-x} = 2 \cdot 2^{-x} = 2 \cdot \left(\frac{1}{2}\right)^x$$

- **Direção:** a base $\frac{1}{2}$ está entre 0 e 1, então a função é **decrescente** — cai pela metade a cada unidade de $x$: $f(0) = 2$, $f(1) = 1$, $f(2) = \frac{1}{2}$.
- **Eixo y:** $f(0) = 2^1 = 2$, ponto **$(0, 2)$**.

## Função logarítmica

### Questão 14
Calcule $\log_{25}(0{,}008)$.

Chamando o resultado de $x$: $25^x = 0{,}008$. Como $0{,}008 = \frac{8}{1000} = \frac{1}{125} = 5^{-3}$ e $25 = 5^2$:

$$5^{2x} = 5^{-3} \quad\Rightarrow\quad x = -\frac{3}{2}$$

### Questão 15
Sendo $a = \log 2$ e $b = \log 3$, escreva $\log 15$ em função de $a$ e $b$.

Como $15 = \frac{30}{2} = \frac{3 \cdot 10}{2}$ e $\log 10 = 1$:

$$\log 15 = \log 3 + \log 10 - \log 2 = b + 1 - a$$

**$\log 15 = 1 - a + b$**. Conferindo com os valores: $1 - 0{,}3010 + 0{,}4771 = 1{,}1761$, que é o valor de $\log 15$.

### Questão 16
Resolva $2^{3x-2} = 3^{2x+1}$.

As bases são diferentes, então aplicamos logaritmo dos dois lados e a propriedade $\log(m^k) = k \log m$:

$$(3x - 2)\log 2 = (2x + 1)\log 3$$

Separando os termos com $x$:

$$3x\log 2 - 2x\log 3 = 2\log 2 + \log 3$$

$$x(\log 8 - \log 9) = \log 4 + \log 3 \quad\Rightarrow\quad x = \frac{\log 12}{\log \frac{8}{9}}$$

Numericamente: $x = \frac{1{,}0792}{-0{,}0512} \approx -21{,}10$.

### Questão 17
Determine o domínio e a raiz de $f(x) = \log_2(x - 1)$.

- **Domínio:** o logaritmando precisa ser positivo: $x - 1 > 0 \Rightarrow x > 1$, isto é, o intervalo $(1, +\infty)$.
- **Raiz:** $\log_2(x - 1) = 0 \Rightarrow x - 1 = 2^0 = 1 \Rightarrow x = 2$, que pertence ao domínio.

### Questão 18
Resolva $\log_{x-1}(x^3 - x^2 + x - 3) = 3$.

**Condições de existência:** a base precisa ser positiva e diferente de 1 ($x > 1$ e $x \neq 2$) e o logaritmando precisa ser positivo.

Pela definição de logaritmo, $(x - 1)^3 = x^3 - x^2 + x - 3$. Desenvolvendo o cubo:

$$x^3 - 3x^2 + 3x - 1 = x^3 - x^2 + x - 3$$

$$-2x^2 + 2x + 2 = 0 \quad\Rightarrow\quad x^2 - x - 1 = 0 \quad\Rightarrow\quad x = \frac{1 \pm \sqrt{5}}{2}$$

- $x = \frac{1 - \sqrt{5}}{2} \approx -0{,}618$: a base $x - 1$ fica negativa, então é **descartada**.
- $x = \frac{1 + \sqrt{5}}{2} \approx 1{,}618$: a base vale $\approx 0{,}618$ (positiva e diferente de 1) e o logaritmando, que é igual a $(x - 1)^3$, vale $\approx 0{,}236 > 0$.

**Solução: $x = \frac{1 + \sqrt{5}}{2}$**, o número de ouro.

## Funções trigonométricas

### Questão 19
Converta 300° para radianos.

$$300^\circ \cdot \frac{\pi}{180^\circ} = \frac{300\pi}{180} = \frac{5\pi}{3} \text{ rad}$$

### Questão 20
Converta $\frac{5\pi}{6}$ rad para graus.

$$\frac{5\pi}{6} \cdot \frac{180^\circ}{\pi} = \frac{5 \cdot 180^\circ}{6} = 150^\circ$$

### Questão 21
Resolva $\sin(2x - \pi) = 0{,}5$.

Subtrair $\pi$ de um ângulo troca o sinal do seno: $\sin(\theta - \pi) = -\sin\theta$. A equação fica:

$$-\sin(2x) = \frac{1}{2} \quad\Rightarrow\quad \sin(2x) = -\frac{1}{2}$$

O seno vale $-\frac{1}{2}$ nos ângulos $\frac{7\pi}{6}$ (3º quadrante) e $\frac{11\pi}{6}$ (4º quadrante), mais as voltas completas:

$$2x = \frac{7\pi}{6} + 2k\pi \quad\text{ou}\quad 2x = \frac{11\pi}{6} + 2k\pi$$

$$x = \frac{7\pi}{12} + k\pi \quad\text{ou}\quad x = \frac{11\pi}{12} + k\pi, \quad k \in \mathbb{Z}$$

No intervalo $[0, 2\pi)$, as soluções são $\frac{7\pi}{12}$, $\frac{11\pi}{12}$, $\frac{19\pi}{12}$ e $\frac{23\pi}{12}$.

### Questão 22
Determine o domínio, a imagem, o período e a amplitude de $f(x) = \sin(3x - \pi)$.

Comparando com a forma $f(x) = A\sin(Bx + C)$: $A = 1$, $B = 3$ e $C = -\pi$.

- **Domínio:** $\mathbb{R}$ — o seno existe para qualquer número real.
- **Imagem:** $[-1, 1]$.
- **Período:** $T = \frac{2\pi}{|B|} = \frac{2\pi}{3}$.
- **Amplitude:** $|A| = 1$.

O $-\pi$ só desloca o gráfico na horizontal (na verdade, $f(x) = -\sin 3x$), sem alterar imagem, período ou amplitude.
