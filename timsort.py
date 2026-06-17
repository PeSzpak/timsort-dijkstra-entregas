# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# timsort.py — Implementação manual do TimSort
#
# O TimSort é o algoritmo padrão do Python (sorted() e list.sort()).
# Combinação de Insertion Sort (pra listas pequenas) + Merge Sort (listas grandes).
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def insertion_sort(arr, esquerda, direita, chave):
    """
    Ordena o trecho arr[esquerda..direita] com Insertion Sort.

    Funciona igual a organizar cartas na mão: pega uma carta,
    vai empurrando as maiores pra direita até achar o lugar certo.

    O TimSort chama isso nos pedaços de até MIN_RUN elementos,
    porque pra listas pequenas o Insertion Sort tem menos overhead.
    """
    for i in range(esquerda + 1, direita + 1):
        elemento_atual = arr[i]
        j = i - 1
        while j >= esquerda and chave(arr[j]) > chave(elemento_atual):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elemento_atual


def merge(arr, esquerda, meio, direita, chave):
    """
    Junta dois pedaços JÁ ordenados em um único pedaço ordenado.

    Ideia: duas filas de pessoas organizadas por altura. Compara o
    primeiro de cada fila e coloca o menor na fila final, até esvaziar as duas.
    """
    parte_esq = arr[esquerda:meio + 1]
    parte_dir = arr[meio + 1:direita + 1]

    i = j = 0
    k = esquerda

    while i < len(parte_esq) and j < len(parte_dir):
        if chave(parte_esq[i]) <= chave(parte_dir[j]):
            arr[k] = parte_esq[i]
            i += 1
        else:
            arr[k] = parte_dir[j]
            j += 1
        k += 1

    while i < len(parte_esq):
        arr[k] = parte_esq[i]
        i += 1
        k += 1

    while j < len(parte_dir):
        arr[k] = parte_dir[j]
        j += 1
        k += 1


def timsort(arr, chave=lambda x: x):
    """
    TimSort — o algoritmo principal.

    Divide em pedaços de até MIN_RUN = 32 elementos ('runs'),
    ordena cada um com Insertion Sort, depois faz Merge progressivo
    até ter tudo em ordem.

    Complexidade:
    - Melhor caso: O(n)       — lista já ordenada
    - Médio/Pior:  O(n log n) — garantido
    """
    MIN_RUN = 32
    n = len(arr)

    # Fase 1: Insertion Sort nos pedaços pequenos
    for inicio in range(0, n, MIN_RUN):
        fim = min(inicio + MIN_RUN - 1, n - 1)
        insertion_sort(arr, inicio, fim, chave)

    # Fase 2: Merge progressivo (32 → 64 → 128 → ...)
    tamanho = MIN_RUN
    while tamanho < n:
        for esquerda in range(0, n, 2 * tamanho):
            meio = min(n - 1, esquerda + tamanho - 1)
            direita = min(n - 1, esquerda + 2 * tamanho - 1)
            if meio < direita:
                merge(arr, esquerda, meio, direita, chave)
        tamanho *= 2

    return arr
