# # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# mapa.py — Dados do grafo (mapa da cidade)
#
# Cenário: motoboy sai do restaurante 'R' e quer saber o caminho
# mais curto para cada ponto de entrega na cidade.
#
# Diagrama do mapa (distâncias em km):
#
#        R ----3---- A ---- 4 ---- E
#        |          /|             |
#        2        5  2             1
#        |      /    |             |
#        B --- 6 ---- C ---- 3 --- D
#         \                        |
#          2                       5
#           \                      |
#             F ------- 7 -------- G
#
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Grafo como lista de adjacência:
# cada nó tem uma lista de tuplas (vizinho, distância_em_km)
MAPA_CIDADE = {
    'R': [('A', 3), ('B', 2)],
    'A': [('R', 3), ('E', 4), ('C', 2), ('B', 5)],
    'B': [('R', 2), ('A', 5), ('C', 6), ('F', 2)],
    'C': [('A', 2), ('B', 6), ('D', 3)],
    'D': [('C', 3), ('E', 1), ('G', 5)],
    'E': [('A', 4), ('D', 1)],
    'F': [('B', 2), ('G', 7)],
    'G': [('F', 7), ('D', 5)],
}
