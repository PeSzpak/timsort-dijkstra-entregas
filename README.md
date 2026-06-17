# TimSort + Dijkstra — Seminário de Algoritmos

Seminário apresentado para a Professora Paula Fernanda.
**Tema:** Aplicação prática do TimSort num algoritmo de grafos (Dijkstra).

---

## O que esse projeto faz

Simula o sistema de rotas de um motoboy de entrega. Dado um mapa de cruzamentos e ruas com distâncias, o programa encontra o **caminho mais curto** entre o restaurante e cada ponto de entrega usando o **algoritmo de Dijkstra**.

O **TimSort** entra como peça fundamental dentro do Dijkstra: ele ordena a lista de vizinhos de cada nó antes de processá-los, garantindo que os caminhos mais curtos sejam explorados primeiro.

---

## Estrutura dos arquivos

```
Exemplo-TimSort/
├── timsort_dijkstra.py   # código principal (TimSort + Dijkstra + prova real)
└── README.md             # este arquivo
```

---

## Como rodar

Só precisa do Python 3 instalado (nenhuma biblioteca externa necessária):

```bash
python3 timsort_dijkstra.py
```

---

## O que o programa exibe

**1. Demonstração do TimSort**
Mostra o TimSort ordenando uma lista de arestas por distância, e compara o resultado com o `sorted()` nativo do Python (que também é TimSort por baixo) pra provar que a implementação está correta.

**2. Dijkstra passo a passo**
Log detalhado de cada decisão: qual nó foi visitado, quais vizinhos foram ordenados pelo TimSort, e quais distâncias foram atualizadas.

**3. Resultado final**
Tabela com a menor distância e o caminho completo do restaurante (`R`) até cada ponto da cidade.

**4. Prova real**
Calcula manualmente (soma a soma) todos os caminhos possíveis entre `R` e `D`, encontra o menor, e compara com o que o Dijkstra retornou. Se baterem, confirma que o algoritmo está certo.

**5. Benchmark**
Mede o tempo do TimSort manual vs o `sorted()` do Python em listas de 100, 500 e 1000 elementos.

---

## Mapa da cidade usado no exemplo

```
        R ----3---- A ----4---- E
        |          /|           |
        2        5  2           1
        |      /    |           |
        B ---6---- C ----3---- D
         \                     |
          2                    5
           \                   |
             F -------7------- G
```

Cada letra é um cruzamento. Os números são a distância em km entre eles.

---

## Por que TimSort + Dijkstra?

O Dijkstra precisa, a cada nó visitado, processar os vizinhos em alguma ordem. Ordenar esses vizinhos por peso (distância) com TimSort antes de processar garante que exploramos os caminhos mais promissores primeiro — o que complementa bem a lógica do algoritmo.

Além disso, o TimSort é eficiente justamente em listas parcialmente ordenadas, que é exatamente o que tende a acontecer num grafo real onde as distâncias variam pouco entre vizinhos próximos.

---

## Complexidade

| Algoritmo         | Melhor caso | Médio     | Pior caso |
|------------------|-------------|-----------|-----------|
| TimSort          | O(n)        | O(n log n)| O(n log n)|
| Dijkstra (puro)  | —           | O(V²)     | O(V²)     |
| Dijkstra + heap  | —           | O((V+E) log V) | O((V+E) log V) |

> V = número de vértices, E = número de arestas

---

## Resultado esperado ao rodar

```
Destino    Distância    Caminho completo
A          3            R → A
B          2            R → B
C          5            R → A → C
D          8            R → A → C → D
E          7            R → A → E
F          4            R → B → F
G          11           R → B → F → G

✅ PROVA REAL APROVADA — o Dijkstra encontrou a distância mínima correta!
```
