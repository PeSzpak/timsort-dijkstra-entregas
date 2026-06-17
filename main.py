# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# main.py — Ponto de entrada do programa
#
# Roda tudo em ordem:
#   1. Demonstração do TimSort isolado
#   2. Dijkstra com log passo a passo
#   3. Resultado final (tabela de distâncias)
#   4. Prova real (verificação manual)
#   5. Benchmark de desempenho
#
# Como rodar: python3 main.py
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from mapa import MAPA_CIDADE
from dijkstra import dijkstra, imprimir_resultado
from demonstracao import demonstracao_timsort, prova_real, benchmark


def main():
    print("\n" + "="*55)
    print("  Seminário — TimSort aplicado ao Dijkstra")
    print("  Exemplo: Sistema de Rotas de Entrega")
    print("="*55)

    # 1. Mostra o TimSort funcionando de forma isolada
    demonstracao_timsort()

    # 2. Roda o Dijkstra com log detalhado de cada passo
    distancias, anteriores, passos = dijkstra(MAPA_CIDADE, 'R')
    for passo in passos:
        print(passo)

    # 3. Tabela de resultados finais
    imprimir_resultado(distancias, anteriores, 'R')

    # 4. Prova real — verifica manualmente se o resultado está certo
    prova_real()

    # 5. Benchmark de desempenho
    benchmark()

    print(f"\n{'='*55}")
    print(f"  FIM")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
