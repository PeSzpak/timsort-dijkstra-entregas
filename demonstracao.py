# =============================================================================
# demonstracao.py — Demonstrações, prova real e benchmark
#
# Funções que provam que o TimSort e o Dijkstra estão funcionando certo.
# =============================================================================

import time
import math
import random
from timsort import timsort
from dijkstra import dijkstra, reconstruir_caminho
from mapa import MAPA_CIDADE


def demonstracao_timsort():
    """
    Mostra o TimSort ordenando uma lista de arestas e compara
    com o sorted() nativo do Python (que também é TimSort por baixo).
    """
    print(f"\n{'='*55}")
    print(f"  DEMONSTRAÇÃO DO TIMSORT")
    print(f"{'='*55}")

    arestas = [('E', 4), ('C', 2), ('B', 5), ('D', 1), ('A', 3)]
    copia = arestas[:]

    print(f"\n  Lista original:  {arestas}")
    timsort(arestas, chave=lambda x: x[1])
    print(f"  TimSort manual:  {arestas}")

    arestas_py = sorted(copia, key=lambda x: x[1])
    print(f"  sorted() Python: {arestas_py}")

    if arestas == arestas_py:
        print(f"\n  ✅ Resultados idênticos — implementação correta!")
    else:
        print(f"\n  ❌ Resultados diferentes — tem algo errado!")


def prova_real():
    """
    Calcula manualmente todas as rotas possíveis de R até D,
    encontra a menor e compara com o que o Dijkstra retornou.

    Caminhos possíveis (sem ciclos):
      R → A → C → D         = 3+2+3 = 8 km
      R → A → E → D         = 3+4+1 = 8 km
      R → B → C → D         = 2+6+3 = 11 km
      R → B → F → G → D     = 2+2+7+5 = 16 km
      R → A → B → C → D     = 3+5+6+3 = 17 km
    Menor esperado: 8 km
    """
    print(f"\n{'='*55}")
    print(f"  PROVA REAL — verificação manual de R → D")
    print(f"{'='*55}")

    caminhos = {
        'R → A → C → D':     [3, 2, 3],
        'R → A → E → D':     [3, 4, 1],
        'R → B → C → D':     [2, 6, 3],
        'R → B → F → G → D': [2, 2, 7, 5],
        'R → A → B → C → D': [3, 5, 6, 3],
    }

    print(f"\n  Calculando manualmente:")
    totais = {}
    for nome, pesos in caminhos.items():
        total = sum(pesos)
        totais[nome] = total
        calc = ' + '.join(str(p) for p in pesos)
        print(f"  {nome}: {calc} = {total} km")

    menor = min(totais.values())
    print(f"\n  Menor manual: {menor} km")
    for k, v in totais.items():
        if v == menor:
            print(f"    → {k}")

    # roda o Dijkstra e verifica
    distancias, anteriores, _ = dijkstra(MAPA_CIDADE, 'R')
    caminho = reconstruir_caminho(anteriores, 'R', 'D')
    dist_alg = distancias['D']

    print(f"\n  Dijkstra: {dist_alg} km | {' → '.join(caminho)}")

    if dist_alg == menor:
        print(f"\n  ✅ PROVA REAL APROVADA — resultado correto!")
    else:
        print(f"\n  ❌ ERRO — resultado não confere!")

    return dist_alg == menor


def benchmark():
    """
    Mede o tempo do TimSort manual vs sorted() do Python
    em listas de tamanhos crescentes.
    """
    print(f"\n{'='*55}")
    print(f"  BENCHMARK — TimSort manual vs sorted() Python")
    print(f"{'='*55}")

    for n in [100, 500, 1000]:
        dados = [(f'no_{i}', random.randint(1, 1000)) for i in range(n)]
        copia = dados[:]

        t0 = time.perf_counter()
        timsort(dados, chave=lambda x: x[1])
        t1 = time.perf_counter()

        t2 = time.perf_counter()
        sorted(copia, key=lambda x: x[1])
        t3 = time.perf_counter()

        print(f"\n  n={n}:")
        print(f"    TimSort manual: {(t1-t0)*1000:.3f} ms")
        print(f"    sorted() Python: {(t3-t2)*1000:.3f} ms")
        print(f"    (Python é mais rápido pois está implementado em C)")
