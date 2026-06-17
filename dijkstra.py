# =============================================================================
# dijkstra.py — Algoritmo de menor caminho
#
# Dado um ponto de partida num grafo, calcula a distância mínima
# para todos os outros nós. Criado por Edsger Dijkstra em 1956.
# Requer pesos não-negativos nas arestas.
# =============================================================================

import math
from timsort import timsort


def dijkstra(grafo, origem):
    """
    Roda o Dijkstra a partir de 'origem' no grafo.

    O grafo é um dicionário: { 'A': [('B', 5), ('C', 2)], ... }

    Aqui o TimSort entra: antes de processar os vizinhos de cada nó,
    ordena a lista de vizinhos por distância. Assim exploramos
    sempre os caminhos mais curtos primeiro.

    Retorna:
    - distancias: menor distância da origem a cada nó
    - anteriores: de onde viemos pra chegar em cada nó (pra reconstruir o caminho)
    - passos:     log detalhado de cada decisão (usado na prova real)
    """
    distancias = {no: math.inf for no in grafo}
    distancias[origem] = 0

    anteriores = {no: None for no in grafo}
    nao_visitados = set(grafo.keys())
    passos = []

    passos.append(f"\n{'='*55}")
    passos.append(f"  DIJKSTRA — partindo de '{origem}'")
    passos.append(f"{'='*55}")

    while nao_visitados:
        # pega o nó não visitado com menor distância conhecida
        no_atual = min(nao_visitados, key=lambda n: distancias[n])

        # se a menor distância disponível ainda é infinito,
        # o resto dos nós é inacessível a partir da origem
        if distancias[no_atual] == math.inf:
            break

        nao_visitados.remove(no_atual)
        passos.append(f"\n  Visitando '{no_atual}' | dist. acumulada: {distancias[no_atual]} km")

        # ordena os vizinhos com TimSort por distância antes de processar
        vizinhos = list(grafo[no_atual])
        timsort(vizinhos, chave=lambda x: x[1])
        passos.append(f"    Vizinhos (TimSort): {vizinhos}")

        for (vizinho, peso) in vizinhos:
            if vizinho in nao_visitados:
                nova_dist = distancias[no_atual] + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    anteriores[vizinho] = no_atual
                    passos.append(f"    ✓ '{vizinho}' atualizado para {nova_dist} km")

    return distancias, anteriores, passos


def reconstruir_caminho(anteriores, origem, destino):
    """
    Reconstrói o caminho percorrendo 'anteriores' de trás pra frente.

    Exemplo: pra chegar em D vim de C, pra chegar em C vim de A, origem é A.
    Então o caminho é A → C → D.
    """
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    caminho.reverse()
    return caminho if caminho[0] == origem else []


def imprimir_resultado(distancias, anteriores, origem):
    """Exibe a tabela de resultados: menor distância e caminho até cada nó."""
    print(f"\n{'='*55}")
    print(f"  RESULTADO — partindo de '{origem}'")
    print(f"{'='*55}")
    print(f"  {'Destino':<10} {'Distância':<14} {'Caminho'}")
    print(f"  {'-'*48}")
    for destino in sorted(distancias):
        if destino == origem:
            continue
        dist = distancias[destino]
        if dist == math.inf:
            print(f"  {destino:<10} {'INACESSÍVEL':<14}")
        else:
            caminho = reconstruir_caminho(anteriores, origem, destino)
            print(f"  {destino:<10} {dist:<14} {' → '.join(caminho)}")
